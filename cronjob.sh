METADATA_VALUE1=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/kek -H "Metadata-Flavor: Google")
METADATA_VALUE2=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/kak -H "Metadata-Flavor: Google")
METADATA_VALUE3=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/kok -H "Metadata-Flavor: Google")

* * * * * PGPASSWORD=$METADATA_VALUE1 psql -U $METADATA_VALUE2 -d group3db --host $METADATA_VALUE3 -c "SELECT SUM(AGE(ended,started)) AS hoursum FROM testilog WHERE date(started) = CURRENT_DATE;" > dailyhour.txt
* * * * * PGPASSWORD=$METADATA_VALUE1  psql -U $METADATA_VALUE2 -d group3db --host $METADATA_VALUE3 -c "SELECT * FROM testilog WHERE date(started) = CURRENT_DATE;" > dailyactivities.txt

