import arxiv

def download_arxiv_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    
    for result in search.results():
        print(f"Downloading {result.title}")
        result.download_pdf(dirpath='arxiv_papers')
        print(f"Saved to arxiv_papers/{result.get_pdf_filename()}")

# Example usage
download_arxiv_papers('Foundation language model development', max_results=20)
