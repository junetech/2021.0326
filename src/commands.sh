# python main.py Flexiblejobshop CP 3600 1 20 Google 8 "../data/Flexiblejobshop/Old Benchmarks" ../Outputs/Flexiblejobshop/Old_20250412_Google_8
# python main.py Flexiblejobshop CP 3600 1 20 Google 8 "../data/Flexiblejobshop/New" ../Outputs/Flexiblejobshop/New_20250412_Google_8
# python main.py Flexiblejobshop CP 3600 1 20 CPLEX 8 "../data/Flexiblejobshop/Old Benchmarks" ../Outputs/Flexiblejobshop/Old_20250412_CPO_8
# python main.py Flexiblejobshop CP 3600 1 20 CPLEX 8 "../data/Flexiblejobshop/New" ../Outputs/Flexiblejobshop/New_20250412_CPO_8
# uv run main.py Hybridflowshop CP 10 0 1 CPLEX 8 ../data/Hybridflowshop ../Outputs/Hybridflowshop/20250716_CPO_8_10s
uv run main.py Hybridflowshop CP 3600 1 1440 CPLEX 8 ../data/Hybridflowshop ../Outputs/Hybridflowshop/20250716_CPO_8_3600s
