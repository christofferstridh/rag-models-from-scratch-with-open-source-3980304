import gc

from database_connect_embeddings import TextEmbedding

def search_embeddings(query_embedding, session, limit=5):
    results = session.query(TextEmbedding.id, TextEmbedding.sentence_number, TextEmbedding.content, TextEmbedding.file_name, TextEmbedding.embedding.cosine_distance(query_embedding).label('distance')).order_by('distance').limit(limit).all()
    return results