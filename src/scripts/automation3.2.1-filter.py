import re

input_file = "results.txt"
output_file = "results-filter.txt"

# Pattern to skip examtopics discussion links
skip_pattern = re.compile(r"examtopics\.com/discussions/amazon/view/")

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for idx, line in enumerate(infile, start=1):
        url = line.strip().strip("',\"")

        if not url:
            continue

        # Skip unwanted examtopics format
        if skip_pattern.search(url):
            continue

        # Write index : url
        outfile.write(f"{idx} : {url}\n")

print(f"Output written to {output_file}")