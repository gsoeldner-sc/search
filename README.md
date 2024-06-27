# Using Google Search API from a Python App

## Step 1: Set up a Google Cloud Project and Enable the Custom Search JSON API
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Go to the [Custom Search JSON API](https://console.developers.google.com/apis/library/customsearch.googleapis.com) page.
4. Enable the API for your project.
5. Set up billing if required (some usage is free, but higher usage may incur costs).

## Step 2: Create an API Key
1. Go to the [Credentials page](https://console.developers.google.com/apis/credentials) in the Google Cloud Console.
2. Click "Create credentials" and select "API key".
3. Copy the generated API key and store it securely.

## Step 3: Set up a Custom Search Engine (CSE)
1. Go to the [Custom Search Engine](https://cse.google.com/cse/) page.
2. Click "Add" to create a new search engine.
3. Define the sites you want to search or set it to search the entire web.
4. After creating the search engine, get the Search Engine ID (cx parameter).

## Step 4: Retrieve the Search Engine ID (cx)
1. Visit [Custom Search Engine](https://cse.google.com/cse/) and log in with your Google account.
2. Select the name of the search engine for which you want to retrieve the ID.
3. Find the `Search engine ID`, which looks something like this:

# Costing
https://developers.google.com/custom-search/v1/overview

Custom Search JSON API provides 100 search queries per day for free. If you need more, you may sign up for billing in the API Console. Additional requests cost $5 per 1000 queries, up to 10k queries per day.
