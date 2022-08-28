# Run with . ./props_to_env.sh secretprops.properties 0

DEBUG=${2:-1}

function build_export {
    # First pipe filters comment lines
    # Second pipe filters $ lines
    # Third pipe filters on uppercase props only
    cat $1 | awk '!/^\s*#/' | awk '!/^\s*$/' | awk '/^[A-Z]+/' | while IFS='' read -r line; do
        KEY=$(echo "$line" | cut -d '=' -f 1)
        VALUE=$(echo "$line" | cut -d '=' -f 2-)
        echo "export $KEY=$VALUE"
    done
}

if [[ $DEBUG == 0 ]]
then
    echo "Applying to env..."
    eval "$(build_export $1)"
    echo "Completed."
else
    echo "Showing built env vars that would be sent:"
    echo "$(build_export $1)"
fi

