

pseudo = "yassine"

print(f"votre resultat {pseudo}:")
 
level_obligatoire=15
level=12
mes_points=20
points_obligatoires=50
if mes_points>=points_obligatoires and level>=level_obligatoire:
  print ("felecitation! vous avez deverouillé le prochain niveau")
  
if mes_points<=49:
  
  if mes_points >= 40:
    print ("desolé mais il vous reste 10 points pour deverrouiller le prochain niveau :(")
  elif mes_points >= 30:
    print ("desolé mais il vous reste 20 points pour deverrouiller le prochain niveau :(")
  elif mes_points >= 20:
    print ("desolé mais il vous reste 30 points pour deverrouiller le prochain niveau :(")
  elif mes_points >= 10:
    print ("desolé mais il vous reste 40 points pour deverrouiller le prochain niveau :(")
  else:  
    print("desolé mais vous aves VRAIMENT pas beaucoup de points")


if level<=14:
  if level == 14:
    print ("desolé mais il vous reste 1 level pour deverrouiller le prochain niveau :(")
  elif level == 13:
    print ("desolé mais il vous reste 2 level pour deverrouiller le prochain niveau :(")
  elif level == 12:
    print ("desolé mais il vous reste 3 level pour deverrouiller le prochain niveau :(")
  elif level == 11 :
    print ("desolé mais il vous reste 4 level pour deverrouiller le prochain niveau :(")
  else: 
    print("desolé mais vous aves VRAIMENT pas beaucoup de level")


	

  








