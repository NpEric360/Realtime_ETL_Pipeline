
: :If you don't have an elastic ip set, and you are frequently restarting the EC2 instance:


@echo off
:: Batch script to prompt user for an IP address and save it as a default


:: Check if the EC2 key-pair is already set
if defined EC2_KEY_PAIR (
    echo Default KEY_PAIR .PEM file is SET TO: %EC2_KEY_PAIR%
) else (
    echo Default key-pair is not set.
)

set /p new_keypair=Enter the key-pair name (e.g., project-3-stock-market.pem) or press Enter to keep the current default):

:: Check if the user provided a new IP address
if not "%new_keypair%"=="" (
    :: Set the new IP address as the default
    setx EC2_KEY_PAIR "%new_keypair%"
    echo Default EC2 Key pair set to: %new_keypair%
) else (
    echo Keeping the current default IP address.
)


:: Check if the IP address environment variable is already set
if defined IP_ADDRESS (
    echo Default IP address is set to: %IP_ADDRESS%
) else (
    echo Default IP address is not set.
)

set /p new_ip=Enter the SSH IP address (or press Enter to keep the current default): 

:: Check if the user provided a new IP address
if not "%new_ip%"=="" (
    :: Set the new IP address as the default
    setx IP_ADDRESS "%new_ip%"
    echo Default IP address set to: %new_ip%
) else (
    echo Keeping the current default IP address.
)

:: Rest of your script goes here, using %IP_ADDRESS% for the IP address as needed

:: Batch script to run SSH command

ssh -i %EC2_KEY_PAIR% %IP_ADDRESS%