
# Multi-agent system using Azure AI to process user queries through a pipeline:
# 1. Code Reader Agent - analyzes input
# 2. Diagram Creator - generates visual representation

import asyncio
import os
from dotenv import load_dotenv

from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from semantic_kernel.agents import AzureAIAgent


# Load configuration from .env file
load_dotenv()

# ----- Agent IDs Configuration -----
# Code Reader Agent (Agent 1)
AGENT1_ID = "asst_iBpw6d3HNpRgWD7Wj2lxKu3V"

# Diagran Creator (Agent 2)
AGENT2_ID = "asst_wgTkzfhlE8qsg48GphK2qULt"

PROJECT_CONN_STR = os.environ.get("AZURE_AI_PROJECT_CONNECTION_STRING")
print(f"Project connection string: {PROJECT_CONN_STR}")

if not PROJECT_CONN_STR:
    raise ValueError("Azure AI Project connection string not found in environment variables. Please set AZURE_AI_PROJECT_CONNECTION_STRING in your .env file.")

async def main():
    # Prompt the user for a query 
    user_query = input("Enter your query")

    # Initialize credentials and the Azure AI Projects client
    credential = DefaultAzureCredential()
    try:
        project_client = AIProjectClient.from_connection_string(
            conn_str=PROJECT_CONN_STR,
            credential=credential
        )
        print("✅ Project client initialized.")
    except Exception as e:
        print(f"❌ Error initializing project client: {e}")
        return

    # Use the async context for proper cleanup of the credential and client
    async with credential, AzureAIAgent.create_client(credential=credential) as client:
        # Retrieve pre-created agent definitions for each role
        document_agent_def = await client.agents.get_agent(agent_id=AGENT1_ID)
        summary_agent_def = await client.agents.get_agent(agent_id=AGENT2_ID)

        # Instantiate Semantic Kernel agent objects
        document_agent = AzureAIAgent(client=client, definition=document_agent_def)
        summary_agent = AzureAIAgent(client=client, definition=summary_agent_def)

        # ----- Agent 1: CodeReaderAgent -----
        # Create a thread for Agent 1 and send the user's query as a chat message.
        thread1 = await client.agents.create_thread()
        await document_agent.add_chat_message(
            thread_id=thread1.id,
            message=user_query
        )
        response_doc = await document_agent.get_response(thread_id=thread1.id)
        print("\n[CodeReaderAgent Response]")
        print(response_doc)

        # ----- Agent 2: DiagramCreator -----
        # Responses from Agent 1 and send to Agent 2 for duagran creation.
        combined_info = response_doc.content
        thread3 = await client.agents.create_thread()
        await summary_agent.add_chat_message(
            thread_id=thread3.id,
            message=combined_info
        )
        response_summary = await summary_agent.get_response(thread_id=thread3.id)
        print("\n[DiagramCreator Response]")
        print(response_summary)
        print("\n\n")
        
        # ----- Optional Cleanup: Delete the conversation threads -----
        for thread in [thread1, thread3]:
            try:
                await client.agents.delete_thread(thread.id)
                
                print(f"✅ Project's threads are deleted-{thread.id}")
            except Exception as e:
                print(f"❌ Error deleting thread {thread.id}: {e}")


if __name__ == "__main__":
    asyncio.run(main())