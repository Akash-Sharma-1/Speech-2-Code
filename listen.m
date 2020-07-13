function output = listen(filePath)
    output = system(['python speech2Text.py ' filePath]);
end