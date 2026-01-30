zenity --question \
  --title="Welcome to the Computer Lab!" \
  --text="Looking to customize your desktops? " \
  --ok-label="View Lab Docs" \
  --cancel-label="Dismiss"

if [[ $? -eq 0 ]]; then
  xdg-open https://https://bestdocs.ocf.io/user-docs/desktop-customization/
fi

