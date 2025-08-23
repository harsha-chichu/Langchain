import os
from secret_key import groq_key
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Set the API key
os.environ['GROQ_API_KEY'] = groq_key

# Load the model
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.9
)

parser = StrOutputParser()

def gen_restaurant_name_and_items(cuisine):
    # Step 1: Generate restaurant name
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest only a single fancy name for it. and do not explain about it"
    )
    name_chain = prompt_name | llm | parser

    # Step 2: Use restaurant name to generate menu
    def menu_chain_fn(restaurant_name):
        prompt_menu = PromptTemplate(
            input_variables=['restaurant_name'],
            template="only suggest the menu items for {restaurant_name} without any explanation. Provide the items in a comma-separated format."
        )
        return prompt_menu.partial(restaurant_name=restaurant_name) | llm | parser

    # Execute both steps
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).strip().replace('"', '')
    menu_items = menu_chain_fn(restaurant_name).invoke({}).strip()

    return {
        "cuisine": cuisine,
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }

if __name__ == "__main__":
    print(gen_restaurant_name_and_items("Italian"))
