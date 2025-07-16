from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

def create_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    return splitter.create_documents([text])

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return FAISS.from_documents(chunks, embedding=embeddings)

def load_llm_model():
    model_id = "HuggingFaceTB/SmolLM3-3B"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        load_in_4bit=True
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.3
    )
    return HuggingFacePipeline(pipeline=pipe)

def build_prompt():
    return PromptTemplate(
        input_variables=["text"],
        template="""
You are a UX researcher creating a concise user persona based on Reddit posts by a single user.

Only analyze one user donot try to create persona of multiple users.. Do not repeat Reddit content.

Format:

Username: [Guess if not given]

Personality:
- [Each trait on its own line.]

Hobbies & Interests:
- [List separately with line breaks.]

Life Stage:
- [Short sentence.]

Goals & Motivations:
- [One point per line.]

Frustrations:
- [One point per line.]

Writing Style:
- [One line per observation.]

Demographic Clues:
- [Each clue on its own line.]

Citation:
- ["Short quote from the Reddit text."]

Only return the persona, clearly formatted. If the user is unclear, infer a realistic alias.
"""
    )

def generate_persona(text, llm, prompt_template):
    chunks = create_chunks(text)
    combined_text = "\n\n".join(chunk.page_content.strip() for chunk in chunks)
    qa = LLMChain(llm=llm, prompt=prompt_template)
    response = qa.invoke({"text": combined_text})
    return response["text"].strip()
