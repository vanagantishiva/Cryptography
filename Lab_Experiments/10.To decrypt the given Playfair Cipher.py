message = "MUST SEE YOU OVER CADOGAN WEST COMING AT ONCE"
# Preprocess: remove spaces, replace J with I
msg = message.replace(" ", "").replace("J","I")

print("Prepared message:", msg)
# Split into digraphs and apply Playfair encryption rules



'''
output: 
Prepared message: MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE
'''