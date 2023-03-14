### Format multiple files from command line or vim

    for i in ./*.{php,js,cpp,sh}; do
        vim -c "normal gg=G" -c "x" $i
    done


