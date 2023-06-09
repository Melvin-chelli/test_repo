rm -r fl_logs/img/*
mkdir -p fl_logs/non-malicious/img

# download dataset
python3 utils/dl_dataset.py --dataset mnist

# First case: without malicious updates
# generate partitions
python3 utils/partition_data.py --n_partitions 10 --dataset mnist

# start server and clients
python3 server.py &
sleep 5
python3 client.py --num 0 &
python3 client.py --num 1 & 
python3 client.py --num 2 &
python3 client.py --num 3
mv fl_logs/img/* fl_logs/non-malicious/img/