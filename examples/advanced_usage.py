from omnimind import OmniMind
import asyncio
import os
import json

async def advanced_multi_server_usage():
    # Ensure GOOGLE_API_KEY is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set the GOOGLE_API_KEY environment variable before running this script")

    # Initialize OmniMind with the multi-server config
    agent = OmniMind(config_path="multi_server_config.json", api_key=api_key)
    try:
        # Connect to all servers
        await agent._connect_servers()
        print("Tools loaded:", [tool.name for tool in agent.tools])

        # Step 1: Fetch web content
        fetch_query = "Fetch the content of 'https://marvel.fandom.com/wiki/Stark_Industries_(Earth-616)' and summarize it"
        fetch_response = await agent.invoke(fetch_query)
        summary = fetch_response["messages"][-1].content  # Extract the summary from the last message
        print("\nStep 1 - Web Summary:", summary)

        # Step 2: Store the summary in memory
        memory_query = f"Store this in memory under key 'stark_summary': {summary}"
        await agent.invoke(memory_query)
        print("Step 2 - Stored summary in memory")

        # Step 3: Recall from memory and save to a file
        recall_query = "Recall the value stored under 'stark_summary' and save it to a file named 'stark_summary.txt' in the workspace directory"
        recall_response = await agent.invoke(recall_query)
        print("Step 3 - Recalled and saved to file:", recall_response["messages"][-1].content)

    except Exception as e:
        print(f"Error during execution: {e}")
    finally:
        await agent.close()

if __name__ == "__main__":
    asyncio.run(advanced_multi_server_usage())