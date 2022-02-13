# SET THIS TO YOUR WORKING DIRECTORY
WORKING_DIR="/root"

cd $WORKING_DIR

# Update the local copy of the bots code using the remote
cd ./Discord-Bottobulous-Maximus && git pull -q || git clone https://github.com/RED-M0CKING-LINE/Discord-Bottobulous-Maximus.git

cd $WORKING_DIR
# Now put symbolic links into the project for persistant data, to preserve the data
rm -r ./Discord-Bottobulous-Maximus/config/  # This may break things later on if I store defaults here. Defaults should be hardcoded and then overridden.
ln -s "$(echo $WORKING_DIR)/Bot-Data/config" "./Discord-Bottobulous-Maximus/config"

reboot
