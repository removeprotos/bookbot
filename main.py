def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
        #print(file_contents)





    def count_words(text):
        split_text = text.split()
        words_total = 0
        for word in split_text:
            words_total += 1
        print (f"Total words found: {words_total}", "\n")
    

    def sort_on(item):
        return item["num"]
    

    def count_symbol(text):
        symbol_table = {}
        split_text = text.lower().split()
        for word in split_text:
            for symbol in word:
                if symbol not in symbol_table:
                    symbol_table[symbol] = 1
                else:
                    symbol_table[symbol] += 1
        symbols_list = []
        for key, value in symbol_table.items():
            symbols_list.append({"char": key, "num": value})
        
        sorted_list = []
        sorted_list = sorted(symbols_list, key=sort_on, reverse=True)
        for i in sorted_list: 
            print(i, "\n")

            
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(file_contents)
    count_symbol(file_contents)
    print("--- End report ---")

main()