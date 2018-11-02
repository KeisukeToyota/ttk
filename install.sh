sudo cp -r ttk ~/.ttk

case `dscl localhost -read Local/Default/Users/$USER UserShell | cut -d' ' -f2 | grep 'zsh'` in
*bash*)
echo export PATH='$HOME/.ttk/:$PATH' >> ~/.bash_profile;;
*zsh*)
echo export PATH='$HOME/.ttk/:$PATH' >> ~/.zshrc;;
*)
echo 'unknown login shell...';;
esac
