from phi.agent import Agent
from phi.document.chunking.semantic import SemanticChunking
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes_semantic_chunking", db_url=db_url),
    chunking_strategy=SemanticChunking(),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    knowledge_base=knowledge_base,
    search_knowledge=True,
)

agent.print_response("How to make Thai curry?", markdown=True)
