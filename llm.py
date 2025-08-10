import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def create_analysis_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )
    
    template = """You are an expert at reviewing slide decks for factual and logical inconsistencies.
                Include textual contradictions and contextual logic gaps. Look into EVERY SLIDE.

                Here is the extracted slide text:
                {slides_text}

                Instructions:
                1. Identify any contradictions, numeric mismatches, or contextual inconsistencies.
                2. Specify the slides involved in each issue.
                3. Include deviations from the main claim.
                4. Keep the output concise and focused on the issues.
                5. Output MUST be grouped in this exact format:

                Deck: {deck_name}
                [Slide X] ISSUE: ...
                [Slide X & Slide Y] ISSUE: ...
                """
    
    prompt = PromptTemplate(
        input_variables=["slides_text", "deck_name"],
        template=template
    )
    
    chain = prompt | llm
    return chain

def run_gemini_analysis(slides_text, deck_name):
    chain = create_analysis_chain()
    print(f"[INFO] Analyzing slides {list(slides_text.keys())} from '{deck_name}'...")
    
    try:
        result = chain.invoke({"slides_text": slides_text, "deck_name": deck_name})
        if hasattr(result, 'content'):
            return result.content
        return result.text if hasattr(result, 'text') else str(result)
    except Exception as e:
        print(f"[ERROR] Analysis failed: {str(e)}")
        return f"Deck: {deck_name}\nAnalysis failed: {str(e)}"