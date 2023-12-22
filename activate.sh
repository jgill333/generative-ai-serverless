env_name="venv"
if [ "$1" = "" ]; then
    env_name="venv"
else
    env_name=$1
fi

source $env_name\bin\activate
echo "Virtual environment activated ($env_name)"

