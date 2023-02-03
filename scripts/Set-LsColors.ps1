# ls colors config - used by 'Color' module
$Global:ColorSettings = @{
    General = @{
        ShortenUserFolder = $true;
    }
    File = @{
        DefaultColor = "#f5f5f5";
        Header = @{
            Visible = $true;
            TextColor = "#767676";
            SeparatorsColor = "#767676";
        }
        Path = @{
            Visible = $false;
            TitleColor = "#767676";
            TextColor = "#cccccc";
        }
        Types = @{
            Directory = @{
                Color = "#51a4b8";
            }
            SymbolicLink = @{
                Color = "#49d4e6";
                ShowTarget = $true;
            }
            Hidden = @{
                Color = "#a6a6a6";
                RegEx = "^\.";
            }
            Binary = @{
                Color = "#5d925d";
                RegEx = "\.(exe|jar|msi|pdf|war)$";
            }
            Code = @{
                Color = "#f5f5f5";
                RegEx = "\.(bat|c|cmd|cpp|cs|css|dfm|dpr|h|html|java|js|json|pas|php|pl|ps1|psm1|py|rb|reg|sh|sql|swift|toml|ts|vb|vbs|yaml|yml)$";
            }
            Compressed = @{
                Color = "#c45242";
                RegEx = "\.(7z|gz|rar|tar|zip)$";
            }
            Text = @{
                Color = "#f5f5f5";
                RegEx = "\.(cfg|conf|config|csv|ini|log|markdown|md|txt|xml)$";
            }
        }
    }
};
