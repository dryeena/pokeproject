application=$1
options=$2
cd /code
echo "Setting up python"
sleep 15
pip3 install -r requirements.txt --quiet

echo "Booting app"
if [ "$application" = "gatherer" ]; then
    echo "Launching Gatherer"
    python3 -m src.apps.gatherer
    echo "Gatherer stopped"
fi
if [ "$application" = "analyzer" ]; then
    echo "launching python 1"
    for i in `seq 2 $options`
    do
        echo "launching python $i"
        python3 -m src.apps.analyzer &
    done
    python3 -m src.apps.analyzer

fi
if [ "$application" = "webapp" ]; then
  echo "Waiting 60 seconds for analyzer to populate"
  sleep 60
  gunicorn -b 0.0.0.0:8000 -w $options src.apps.app:app  
fi