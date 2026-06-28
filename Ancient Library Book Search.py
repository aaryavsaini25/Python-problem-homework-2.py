def search_books():
    keyword="python"
    books=(("Python Basics", 250), ("Data Structures", 300), ("Advanced PYTHON", 500) )
    names=()
    pages=()
    titles=[]
    title_page=[]
    for name,page in books:
        names += name,
        pages += page,
        if keyword in name.lower():
            titles.append(name)
            title_page.append(page)
            is_found=True
        else:
            is_found=False
    if is_found==False:
        print("No books found")
    else:
        print("Matching books found.")
    sum=0
    for pg in title_page:
        sum=sum+pg
    display_names=str(names).strip("()")
    display_pages=str(pages).strip("()")
    display_titles=str(titles).strip("[]")
    display_title_page=str(title_page).strip("[]")
    print(f"The names of the books were {display_names}.")
    print(f"Their pages were {display_pages} respectively.")
    print(f"The names that had the word {keyword} on it were {display_titles}.")
    print(f"Their pages were {display_title_page} respectively.The total of these pages were {sum}.")
search_books()