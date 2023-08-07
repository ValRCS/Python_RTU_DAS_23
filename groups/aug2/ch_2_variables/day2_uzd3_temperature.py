celsijs = float(input( f"Cik šobrid ir Tavas istabas temeratūra ?"))
farenheits = 32+celsijs*(9/5)
# we could either use round or use .2f to show 2 digits after comma(.)
print(f"Tavas istabas temperatûra fārenheitos ir: {farenheits:.2f}")