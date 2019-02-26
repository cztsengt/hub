First
cd C:\Users\caleb.tsenytham\Documents\GitHub\hub\examples\image_retraining

Second
python retrain.py \
–-how_many_training_steps 500 \
–-output_graph=/retrained_graph.pb \
--output_labels=/retrained_labels.txt \
–-image_dir=C:/Users/Caleb Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/training_data

python retrain.py \
--how_many_training_steps 500 \
--output_graph=C:/Users/Caleb Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/retrained_graph.pb \
--output_labels=C:/Users/Caleb Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/retrained_labels.txt \
--image_dir=C:/Users/Caleb Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/training_data

python retrain.py \
--how_many_training_steps 500 \
--output_graph=C:/Users/Caleb Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/retrained_graph.pb \
--output_labels=C:/Users/Caleb_Tseng-Tham/Documents/GitHub/hub/examples/image_retraining/retrained_labels.txt \

python retrain.py \
--image_dir=training_data

python retrain.py --image_dir ~/training_data
