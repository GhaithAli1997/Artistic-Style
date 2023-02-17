# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:57:28 2021

@author: ghaith
"""

Leonardo_da_Vinci=" Full Name:Leonardo di ser Piero da Vinci \n Date of Birth:16 Apr 1452\n Date of Death:02 May 1519\n Focus:Paintings, Drawings \n Mediums:Oil, Tempera, Wood, Other \n Subjects:Figure, Landscapes \n Art Movement:Renaissance \n Hometown:Florence, Italy"
#print(Leonardo_da_Vinci)
style_dictionary = {
  1: " Full Name:Leonardo di ser Piero da Vinci \n Date of Birth:16 Apr 1452\n Date of Death:02 May 1519\n Focus:Paintings, Drawings \n Mediums:Oil, Tempera, Wood, Other \n Subjects:Figure, Landscapes \n Art Movement:Renaissance \n Hometown:Florence, Italy",
  2: "Full Name:Michelangelo di Lodovico Buonarroti Simoni\n Date of Birth:06 Mar 1475\n Date of Death:18 Feb 1564 \n Focus:Paintings, Sculpture, Architecture, Drawings\n Mediums:Oil, Wood, Stone, Other\n Subjects:Figure, Fantasy\n Art Movement:Renaissance\n Hometown:Unknown City of Tuscany, Italy\n Living In:Florence, Italy\n Architecture:Saint Peter's Basilica",
  3: "Short Name:Constable\n Date of Birth:11 Jun 1776\n Date of Death:31 Mar 1837\n Focus:Paintings\n Mediums:Oil, Watercolor\n Subjects:Landscapes\n Art Movement:Romanticism\n Hometown:East Bergholt, United Kingdom",
  4: "Full Name:William Hogarth\nShort Name:Hogarth\nDate of Birth:10 Nov 1697\nDate of Death:26 Oct 1764\nFocus:Paintings\nMediums:Oil, Prints, Wood, Other\nSubjects:Figure, Scenery\nArt Movement:Rococo\nHometown:London, United Kingdom",
  5: "Full Name:Vincent Willem van Gogh\nShort Name:Van Gogh\nDate of Birth:30 Mar 1853\nDate of Death:29 Jul 1890\nFocus:Paintings\nMediums:Oil\nSubjects:Figure, Landscapes, Cityscapes, Scenery\nArt Movement:Post-Impressionism\nHometown:Zundert, Netherlands",
  6: "1964",
  7: "Mustang",
  8: "1964"
}


image_dictionary={
    "Mona_Lisa ":"Date of Creation:1506 \n Alternative Names:Portrait of Lisa Gherardini, wife of Francesco del Giocondo, La Gioconda \n Height (cm):77.00\n Length (cm):53.00\n Medium:Oil \n Support:Wood \n Subject:Figure \n Framed:Yes \n Art Movement:Renaissance \n Created by:Leonardo da Vinci\n Current Location:Paris, France\n Displayed at:Musée du Louvre\n Owner:Musée du Louvre",
    "The_Last_Supper":"Date of Creation:1498\n Height (cm):460.00 \n Length (cm):880.00\n Medium:Tempera \n Support:Other \n Subject:Figure \n Framed:No \n Art Movement:Renaissance \n Created by:Leonardo da Vinci \n Current Location: Milan, Italy \n Displayed at:Santa Maria delle Grazie \n Owner:Santa Maria delle Grazie",
    "Virgin_of_the_Rocks":"The Virgin of the Rocks was the first painting produced by\n Leonardo da Vinci after his arrival in Milan.\n He was commissioned to complete \n the work within a year but, as was often the case\n, he over-ran and so a lengthy law suit followed.\n The artist also had disagreements over payment of\n the work and this may be why he embarked on a second version\n to give to the commissioners, as he \n sold the first one elsewhere",
    "Saint_Jerome":"Date of Creation:circa 1480 \n Height (cm):103.00\n Length (cm):75.00 \n Medium:Oil, Tempera \n Support:Wood \n Subject:Figure \n Art Movement:Renaissance\n Created by:Leonardo da Vinci\n Current Location:Vatican City, Holy See (Vatican City State) \n Displayed at:Vatican Museums\n Owner:Vatican Museums ",
    "Virgin_and_Child_with_St_Anne":"Height (cm):168.00\n Length (cm):130.00\n Support:Wood \n Subject:Figure\n Framed:Yes/n Art Movement:Renaissance\n Created by:Leonardo da Vinci \n Current Location:Paris,France\n Displayed at:Musée du Louvre\n Owner:Musée du Louvre",
    "Adorazione_dei_Magi":"Date of Creation:1481\n Height (cm):246.00\n Length (cm):243.00\n Medium:Oil\n Support:Wood\n Subject:Figure\n Assisted By:Domenico Ghirlandaio, Filippino Lippi\n Art Movement:Renaissance\n Created by:Leonardo da Vinci\n Current Location:Florence, Italy\n Displayed at:Galleria degli Uffizi\n Owner:Galleria degli Uffizi",
    "The Manchester Madonna":"Date of Creation:1497\n Height (cm):76.00\n Length (cm):105.00\n Medium:Tempera\n Support:Other\n Subject:Fantasy\n Art Movement:Renaissance\n Created by:Michelangelo\n Current Location:London, United Kingdom\n Displayed at:National Gallery London\n Owner:National Gallery London",
    "Doni Tondo":"Date of Creation:1507\n Medium:Tempera\n Support:Other\n Subject:Figure\n Art Movement:Renaissance\n Created by:Michelangelo\n Current Location:Florence, Italy\n Displayed at:Galleria degli Uffizi\n Owner:Galleria degli Uffizi",
    "Isaiah":"Date of Creation:circa 1512\n Alternative Names:The Prophet Isaiah\n Height (cm):380.00\n Length (cm):365.00\n Support:Other\n Subject:Figure\n Framed:No\n Art Movement:Renaissance\n Created by:Michelangelo\n Current Location:Vatican City, Holy See (Vatican City State)",
    "The Torment of St Anthony":"Date of Creation:1488\n Height (cm):35.00\n Length (cm):47.00\n Medium:Oil, Tempera\n Support:Other\n Subject:Fantasy\n Art Movement:Renaissance\n Created by:Michelangelo\n Current Location:Fort Worth, Texas\n Displayed at:Kimbell Art Museum\n Owner:Kimbell Art Museum",
    "A View at Salisbury from Archdeacon Fisher's House":"Date of Creation:circa 1829\n Height (cm):20.00\n Length (cm):25.10\n Medium:Oil\n Support:Canvas\n Subject:Landscapes\n Framed:Yes\n Art Movement:Romanticism\n Created by:John Constable\n Current Location:London, United Kingdom\n Owner:Victoria and Albert Museum",
    "Salisbury Cathedral and Leadenhall from the River Avon":"Date of Creation:1820\n Height (cm):52.70\n Length (cm):77.00\n Medium:Oil\n Support:Canvas\n Subject:Landscapes\n Art Movement:Romanticism\n Created by:John Constable\n Current Location:London, United Kingdom\n Displayed at:National Gallery London\n Owner:National Gallery London",
    "The Cornfield":"Date of Creation:1826\n Height (cm):143.00\n Length (cm):122.00\n Medium:Oil\n Support:Canvas\n Subject:Landscapes\n Art Movement:Romanticism\n Created by:John Constable\n Current Location:London, United Kingdom\n Displayed at:National Gallery London\n Owner:National Gallery London",
    "A Scene from 'The Tempest":"Date of Creation:circa 1735\nMedium:Oil\nSupport:Canvas\nSubject:Scenery\nArt Movement:Rococo\nCreated by:William Hogarth",
    "Starry Night":"Date of Creation:1889\nHeight (cm):73.70\nLength (cm):92.10\nMedium:Oil\nSupport:Canvas\nSubject:Landscapes\nCharacteristics:Post-impressionism\nFramed:Yes\nArt Movement:Post-Impressionism\nCreated by:Vincent van Gogh\nCurrent Location:New York, New York\nOwner:Museum of Modern Art",
    "Sunflowers":"Date of Creation:1888\nHeight (cm):92.10\nLength (cm):73.00Medium:Oil\nSupport:Canvas\nSubject:Scenery\nFramed:Yes\nArt Movement:Post-Impressionism\nCreated by:Vincent van Gogh\nCurrent Location:London, United Kingdom\nOwner:National Gallery London",
    
    
    }


