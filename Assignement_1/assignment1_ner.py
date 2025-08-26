"""
Assignment 1: Named Entity Recognition (NER) using SpaCy
Student: [Your Name]
Course: Natural Language Processing
Date: August 26, 2025

Objective: Implement Named Entity Recognition on textual data using SpaCy library for English language
to identify and categorize minimum 15-20 entity types.
"""

import spacy
from spacy import displacy
from collections import Counter

def main():
    """
    Assignment 1: Comprehensive Named Entity Recognition Implementation
    Identifies 15+ entity categories using SpaCy English model
    """
    
    print("="*60)
    print("ASSIGNMENT 1: NAMED ENTITY RECOGNITION")
    print("Using SpaCy Library for English Language Processing")
    print("="*60)
    
    # Load English language model
    print("\n1. Loading SpaCy English model...")
    nlp = spacy.load("en_core_web_sm")
    
    # Comprehensive text with multiple entity types for assignment
    text = """
    Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976 in Cupertino, California. 
    As of 2023, the company has a market value of over $3 trillion. The iPhone was first released on June 29, 2007, 
    and current CEO Tim Cook took over from Jobs in 2011. Apple operates in China, India, and throughout Europe.
    
    Microsoft Corporation was founded by Bill Gates and Paul Allen on April 4th, 1975, in Albuquerque, New Mexico.
    The company is now headquartered in Redmond, Washington, and employs over 221,000 people worldwide.
    Microsoft's market capitalization reached $2.8 trillion in early 2024.
    
    Google LLC was established by Larry Page and Sergey Brin while they were PhD students at Stanford University 
    in September 1998. The company went public on August 19, 2004, with an IPO price of $85 per share.
    
    Amazon.com Inc. was founded by Jeff Bezos in July 1994 in Bellevue, Washington. Amazon Web Services (AWS) 
    generates over $80 billion annually and holds approximately 33% of the cloud market share.
    
    Tesla Motors was incorporated on July 1st, 2003, by Martin Eberhard and Marc Tarpenning. 
    Elon Musk joined as chairman in February 2004 and became CEO in 2008.
    
    The United States of America has a population of approximately 331.9 million people as of 2023.
    The U.S. Constitution was ratified on June 21, 1788. The country spans 3.8 million square miles.
    
    NASA launched the James Webb Space Telescope on December 25, 2021, from the Guiana Space Centre in French Guiana.
    The telescope cost $10 billion to develop and is positioned approximately 1.5 million kilometers from Earth.
    
    Barack Obama served as the 44th President of the United States from January 20, 2009, to January 20, 2017.
    He was born on August 4, 1961, in Honolulu, Hawaii, and graduated from Harvard Law School in 1991.
    Obama won the Nobel Peace Prize in 2009 and published his memoir "A Promised Land" in November 2020.
    
    Harvard University, established in 1636, is located in Cambridge, Massachusetts, and has an endowment of 
    $53.2 billion as of 2022. The university has a 3.4% acceptance rate.
    """
    
    # Process the text
    print("\n2. Processing text for Named Entity Recognition...")
    doc = nlp(text)
    
    # Extract all entities
    entities = []
    print("\n3. Named Entities Found:")
    print("-" * 40)
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
        print(f"{ent.text:<25} | {ent.label_}")
    
    # Count entity types
    entity_counts = Counter([label for _, label in entities])
    
    print(f"\n4. Entity Type Distribution:")
    print("-" * 40)
    print(f"Total Entities Found: {len(entities)}")
    print(f"Entity Categories: {len(entity_counts)}")
    
    print(f"\nCategory Breakdown:")
    for label, count in entity_counts.most_common():
        print(f"{label:<12} | {count:>3} entities | {spacy.explain(label)}")
    
    # Generate HTML visualization
    print(f"\n5. Generating HTML Visualization...")
    html_output = displacy.render(doc, style="ent", page=True)
    
    output_file = "assignment1_ner_visualization.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_output)
    
    print(f"✅ HTML visualization saved to '{output_file}'")
    
    # Assignment Results Summary
    print(f"\n" + "="*60)
    print("ASSIGNMENT 1 RESULTS SUMMARY")
    print("="*60)
    print(f"✅ Successfully identified {len(entity_counts)} entity categories")
    print(f"✅ Total named entities processed: {len(entities)}")
    print(f"✅ HTML visualization generated successfully")
    
    # Show all SpaCy NER categories for reference
    print(f"\n6. SpaCy NER Categories Reference:")
    print("-" * 50)
    spacy_labels = [
        ("PERSON", "People, including fictional"),
        ("NORP", "Nationalities or religious or political groups"),
        ("FAC", "Buildings, airports, highways, bridges, etc."),
        ("ORG", "Companies, agencies, institutions, etc."),
        ("GPE", "Countries, cities, states"),
        ("LOC", "Non-GPE locations, mountain ranges, bodies of water"),
        ("PRODUCT", "Objects, vehicles, foods, etc."),
        ("EVENT", "Named hurricanes, battles, wars, sports events"),
        ("WORK_OF_ART", "Titles of books, songs, etc."),
        ("LAW", "Named documents made into laws"),
        ("LANGUAGE", "Any named language"),
        ("DATE", "Absolute or relative dates or periods"),
        ("TIME", "Times smaller than a day"),
        ("PERCENT", "Percentage, including %"),
        ("MONEY", "Monetary values, including unit"),
        ("QUANTITY", "Measurements, as of weight or distance"),
        ("ORDINAL", "first, second, etc."),
        ("CARDINAL", "Numerals that do not fall under other types")
    ]
    
    for label, description in spacy_labels:
        found = "✓" if label in entity_counts else "✗"
        count = entity_counts.get(label, 0)
        print(f"{found} {label:<12} ({count:>2}) - {description}")
    
    print(f"\n" + "="*60)
    print("ASSIGNMENT 1 COMPLETED SUCCESSFULLY!")
    print("="*60)
    
    return entity_counts, doc

if __name__ == "__main__":
    # Execute Assignment 1
    results, processed_doc = main()
    
    # Additional assignment statistics
    print(f"\nFinal Statistics:")
    print(f"- Categories with entities: {len([k for k, v in results.items() if v > 0])}/18")
    print(f"- Most common entity type: {max(results, key=results.get)} ({results[max(results, key=results.get)]} entities)")
    print(f"- Assignment requirement (15+ categories): {'✅ PASSED' if len(results) >= 15 else '❌ NEEDS MORE CATEGORIES'}")
