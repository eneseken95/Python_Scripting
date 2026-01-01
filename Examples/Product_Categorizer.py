def categorize_products(lines):
    categories = {}

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line or line.startswith("#"):
            i += 1
            continue

        if "," in line:
            parts = line.split(",")
            product = parts[0].strip()
            category = parts[1].strip()
        else:
            product = line
            i += 1
            if i < len(lines):
                category = lines[i].strip()
            else:
                i += 1
                continue

        if category not in categories:
            categories[category] = []

        if product not in categories[category]:
            categories[category].append(product)

        i += 1

    for category in categories:
        categories[category].sort()

    return categories


def top_3_categories_by_product_count(categories):
    category_counts = []
    for category, products in categories.items():
        category_counts.append((category, len(products)))

    category_counts.sort(key=lambda x: -x[1])

    return category_counts[:3]


if __name__ == "__main__":
    lines = [
        "apple",
        "fruit",
        "pear",
        "fruit",
        "tomato",
        "vegetable",
        "pepper",
        "vegetable",
        "milk",
        "dairy",
        "yogurt",
        "dairy",
        "apple,fruit",
        "#comment",
    ]

    result = categorize_products(lines)

    print("\nCATEGORIES")
    for category in sorted(result.keys()):
        print(f"{category}: {result[category]}")

    print("\nTOP 3 CATEGORIES BY PRODUCT COUNT")
    top_3 = top_3_categories_by_product_count(result)
    for rank, (category, count) in enumerate(top_3, 1):
        print(f"{rank}. {category} → {count} products")
