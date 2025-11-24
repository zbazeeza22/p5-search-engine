#!/bin/bash
set -Eeuo pipefail

INPUT_DIR="${1:-crawl}"
OUTPUT_DIR="output"

rm -rf output0 output1 output2 output3 output4 "$OUTPUT_DIR"

madoop -input "$INPUT_DIR" -output output0 -mapper ./map0.py -reducer ./reduce0.py
cp output0/part-00000 total_document_count.txt

madoop -input "$INPUT_DIR" -output output1 -mapper ./map1.py -reducer ./reduce1.py

madoop -input output1 -output output2 -mapper ./map2.py -reducer ./reduce2.py

madoop -input output2 -output output3 -mapper ./map3.py -reducer ./reduce3.py

madoop -input output3 -output output4 -mapper ./map4.py -reducer ./reduce4.py

madoop \
  -input output4 \
  -output "$OUTPUT_DIR" \
  -mapper ./map5.py \
  -reducer ./reduce5.py \
  -partitioner ./partition.py \
  -numReduceTasks 3

echo "Output directory: $OUTPUT_DIR"

cp output/part-00000 ../index_server/index/inverted_index/inverted_index_0.txt
cp output/part-00001 ../index_server/index/inverted_index/inverted_index_1.txt
cp output/part-00002 ../index_server/index/inverted_index/inverted_index_2.txt
