copy:
	gcloud compute ssh --command "rm -rf ~/kaggle_speech_recognition/src" --project "mltest-180907" --zone "europe-west1-d" "keras--tf-gpu"
	gcloud compute scp src "keras--tf-gpu":~/kaggle_speech_recognition/src --recurse --zone europe-west1-d --compress

ssh:
	gcloud compute ssh --project "mltest-180907" --zone "europe-west1-d" "keras--tf-gpu"

shutdown:
	gcloud compute ssh --command "sudo shutdown -h now" --project "mltest-180907" --zone "europe-west1-d" "keras--tf-gpu"

download:
	gcloud compute scp "keras--tf-gpu":~/kaggle_speech_recognition/submissions submissions/ --recurse --zone europe-west1-d

start:
	gcloud compute instances start keras--tf-gpu --zone=europe-west1-d

train:
	rm -rf submissions
	mkdir submissions
	rm -rf output
	python3 src/ gcloud train

tensorboard:
	tensorboard --logdir output --port 8888