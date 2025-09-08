def galonLitroiksi(galon) :
      litrat = galon*3.785

      return litrat


galonAnto = float(input(" Anna nestemäärä galloina : "))



while galonAnto>=0 :
    litrat = galonLitroiksi(galonAnto)
    print(f"{galonAnto:0.2f}gallonaa littroina on {litrat:0.2f} litraa")
    galonAnto = float(input(" Anna nestemäärä galloina : "))