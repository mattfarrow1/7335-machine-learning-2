# Previous Final Projects Ranking Script
# https://docs.google.com/document/d/1lsxX5dleP1H5jMkW6nWIDDSaKBkJEL4du7JNsk7x1K0/edit

# Instructions:
# Watch the videos  and reorder the list so if mine was ['Santerre', "Joe", 'Jane', 'Emily']
# If I thought Jane was best video, then Emily then Joe, I would paste in the
# Google Doc: ['Santerre', 'Jane','Emily','Joe']

import numpy as np

previous = ['G. Hudgeons','B. Brewer','Y. Leung','J. Partee','K. Chang','R. Chandna','A. Rajan','D. Kunupudi','S. Godbole','Y. Chu','A. Cattley','M. J. Wolfe','A. Ansari','A. Nguyen','B. Lee','K. Somes','A. Heroy','R. Hazell','B. Arendale','R. Quincy Paul','V. Torres','K. Patterson','L. Zheng','P. Kumar','A. Norman','A. Garapati','C. Henderson','S. Fogelman','J. Munguia','T. Pompo','C. Kim','A. Wilkins','T. Deason','M. Garcia','L. Jiang','B. Wilke','D. Josephs','Z. Gill','R. Talk','S. Mylapore','S. Daggubati','M. Moro','W. Trevino','S. Hayden','J. Au','J. Gipson','J. Pafford','S. Zaheri','M. Ludlow','A. Ho','N. Wittlin','C. Hu','S. Garcia de Alford','J. Vasquez','P. Byrd','G. Kodi','S. Sprague','B.A. Kannan','K. Rollins','N. Gupta','B. Coari','J. Saldana','C. Drake','D. Byrne','S.Gozdzialski','K. Mendonsa','S. Cocke','J.Villanueva','C. Kim','P. Leon','P. Flaming','C. Graves','D.Stroud','Y. S. Kunwar','S. Chew','J. Lancon','V. Viswanathan','S. Samuel','A. Mohan','A. Subramanian','A. Saxena','I. Bakhtiar','D. Geislinger','M. Kuklani','M. Hightower','B. Houssaye','A. Veluchamy','S. Milett','N. Wall','K. Thomas','C. Martinez','S. Gu','K. Dickens','J. Heinen','K. Okiah','M. Palanisamy','N. Brown','L. Sterling','A. Siddiqui','D. Davieau','C. Morgan','L. Cheng','B. Yu','E. Carrera','M. Toolin','M. Rega','J. Lingle','B. Kimbark','R. Bss','R. Simhambhatla','J. Kassof','T. Prasad','N. Rezsonya','M. Shubbar','G. Lane','M. Luzardo','A. Nelson','B. Benefield','J. Flores','A. Schams','J. Knowles','A. Shen','M. Shahini','J. Lubich','M. Pednekar','R. Nagarajan','M. Shulyk','J. Lin','J. Marin','S. Fite','V. Ahir','L. Dajani','A. Burnett','J. Harding','Philip','J.Tan','C. Walenciak','T. Gianelle','A. Pathak','S. Jung','J. Howard','A. Faltesek','L. Clinton','K. Pradeepkumar','R. Djoko','D. Shaw','S. Kennedy','E. Fry','B. Stephan','B.Waite','J. Coate','P. Adams','S.t Miller','K. Ayala','R. Meagher','S. Pillay','A. Mejia','H. Wang','M. Riley','R. McDaniel','H. Nguyen','S.n McWhirter','A. Ruthford','C. Nava','J. Roach','T. Abera','S. Chavan','Y. Zhang','I. Nwaogu','A. Bravo','J. Balson','S. Smith','F. Poon','Balaji','F.Savorgnan','Balaji','Dustin Bracy','Andrew Larsen','D.Clark','A. Roderick','M. Nelson','D. Crouthamel','P. Rai','M. Chinchilla','J. Eysenbach','A.Ghaemmaghami','J. Schueder','M. Kimari','V. Kaniti','E. Lull','D. Ibrahim','A. Vankina','L. Mathew','I. Dhillon','J. Washburn','B. Nayden','W. Arnost','Y. Zhang','S. Prabhala','A. Vel','J. Stacy','J. Nguyen','T. Pengilly','Q. Chau','B. Dakshinamoorthi','N. Dixit','C. Dawson,','J. Vo','J. Rupp','A. Canton','B.  Franklin','P. Huggins','S. Purvis','K. Ghimire','W. Lai','B. Yun','T. Schwebke','S. Onalaja','J. Layne','M. Weatherford','Y. Shin','R. Mitra','S. Moharana','R. Satluri','A. Thobani','P. Attah','G. Kapil']

all_students =['Helene Barrera','Amber Clark','Justin Ehly','Ben Goodwin','BABATUNDE John Olanipekun','Jorge Olmos','Anish Patel','Kenneth Poling','Eric Romero','David Wei','Megan Ball','Jacob Brionez','Rohit Channe','Taifur Chowdhury','Matt Farrow','Blake Freeman','Ana Glaser','Jake Harrison','Juan Nunez','Neddy Nyatome','Tina Pai','Venkata Leela Maruthi Ganesh Vanga','Renfeng Wang','Zachary Zaiken']

results = []

for student in all_students:
  tmp = [student]
  tmp.extend([previous[np.random.randint(len(previous))] for _ in range(15)])
  results.append(tmp)

[['Helene Barrera', 'G. Kodi', 'D.Stroud', 'M. Ludlow', 'B. Wilke', 'J. Harding', 'C. Kim', 'D. Davieau', 'R. Bss', 'J. Eysenbach', 'R. Satluri', 'A. Rajan', 'J. Flores', 'B. Brewer', 'J. Coate', 'Y. S. Kunwar'],
 ['Amber Clark', 'F. Poon', 'D. Geislinger', 'H. Wang', 'A. Rajan', 'S. Fogelman', 'S. Godbole', 'S.t Miller', 'P. Kumar', 'W. Trevino', 'Y. Zhang', 'S. Chew', 'E. Lull', 'P. Kumar', 'S. Mylapore', 'B. Arendale'],
['Justin Ehly', 'S. Purvis', 'M. Toolin', 'B. Brewer', 'J. Balson', 'Dustin Bracy', 'S. Onalaja', 'S. Chavan', 'L. Dajani', 'A. Siddiqui', 'A. Wilkins', 'Y. Leung', 'J. Vo', 'Balaji', 'M. Chinchilla', 'B. Coari'], 
['Ben Goodwin', 'P. Huggins', 'L. Zheng', 'S.t Miller', 'M. Ludlow', 'K. Pradeepkumar', 'M. Pednekar', 'T. Prasad', 'J. Rupp', 'P. Kumar', 'H. Nguyen', 'M. Hightower', 'M. Shubbar', 'A. Mejia', 'L. Zheng', 'A. Ruthford'],
 ['BABATUNDE John Olanipekun', 'D.Stroud', 'I. Dhillon', 'P. Huggins', 'A. Vel', 'S. Onalaja', 'A. Garapati', 'C. Drake', 'A. Heroy', 'W. Arnost', 'E. Fry', 'V. Torres', 'S. Chew', 'R. Hazell', 'M. Nelson', 'P. Flaming'], 
['Jorge Olmos', 'T. Pengilly', 'J. Stacy', 'M. Kuklani', 'L. Zheng', 'L. Jiang', 'S. Garcia de Alford', 'K. Ayala', 'J. Schueder', 'N. Wittlin', 'Y. S. Kunwar', 'A. Schams', 'A. Faltesek', 'M. Nelson', 'G. Lane', 'A. Nelson'],
 ['Anish Patel', 'H. Wang', 'A. Pathak', 'Y. Chu', 'F.Savorgnan', 'D. Ibrahim', 'W. Trevino', 'A. Heroy', 'J. Balson', 'J. Lubich', 'R. Mitra', 'R. Mitra', 'M. Ludlow', 'S. Purvis', 'A. Nguyen', 'M. Moro'],
 ['Kenneth Poling', 'I. Bakhtiar', 'A. Shen', 'A. Canton', 'Y. Chu', 'K. Okiah', 'I. Bakhtiar', 'K. Patterson', 'T. Deason', 'A. Thobani', 'S.Gozdzialski', 'S. Milett', 'D.Stroud', 'D. Byrne', 'A. Veluchamy', 'S.n McWhirter'], 
['Eric Romero', 'C. Dawson,', 'L. Dajani', 'A. Thobani', 'Philip', 'N. Wall', 'J. Nguyen', 'K. Mendonsa', 'A. Norman', 'N. Gupta', 'S. Garcia de Alford', 'R. Satluri', 'P. Rai', 'D. Shaw', 'K. Chang', 'M. Nelson'], 
['David Wei', 'J. Roach', 'A. Rajan', 'A. Pathak', 'W. Arnost', 'M. Ludlow', 'D. Ibrahim', 'A. Mohan', 'R. McDaniel', 'D. Shaw', 'J. Marin', 'Y. Zhang', 'A. Ho', 'A. Nelson', 'A. Roderick', 'Andrew Larsen'], 
['Megan Ball', 'A. Roderick', 'R. Mitra', 'T. Pengilly', 'V. Torres', 'J.Tan', 'D. Kunupudi', 'H. Nguyen', 'C. Walenciak', 'B.  Franklin', 'J. Vasquez', 'A. Garapati', 'F. Poon', 'M. Luzardo', 'P. Byrd', 'Philip'], 
['Jacob Brionez', 'M. Shubbar', 'N. Rezsonya', 'Y. Shin', 'Dustin Bracy', 'S. Chavan', 'J. Rupp', 'B. Nayden', 'R. Quincy Paul', 'F. Poon', 'N. Wittlin', 'S. Milett', 'B. Stephan', 'A. Vel', 'B. Yu', 'M. Shulyk'],
 ['Rohit Channe', 'V. Torres', 'I. Bakhtiar', 'J. Coate', 'M. Palanisamy', 'C. Hu', 'J. Coate', 'J. Layne', 'L. Mathew', 'T. Gianelle', 'D. Geislinger', 'J. Lin', 'B. Yu', 'L. Clinton', 'C. Nava', 'J. Knowles'],
 ['Taifur Chowdhury', 'A. Ansari', 'M. Toolin', 'Y. Zhang', 'P. Rai', 'R. Mitra', 'J. Saldana', 'S.t Miller', 'H. Nguyen', 'C. Morgan', 'Dustin Bracy', 'C. Walenciak', 'T. Pengilly', 'B. Yu', 'I. Bakhtiar', 'S. Sprague'], 
['Matt Farrow', 'A. Bravo', 'N. Brown', 'Y. Zhang', 'G. Kodi', 'K. Chang', 'Philip', 'C. Kim', 'S. Fogelman', 'S. Fogelman', 'K. Ghimire', 'R. Talk', 'Andrew Larsen', 'M. Palanisamy', 'E. Lull', 'S. Garcia de Alford'],
 ['Blake Freeman', 'R. Simhambhatla', 'J. Balson', 'Z. Gill', 'J. Lubich', 'S. Onalaja', 'K. Chang', 'C. Drake', 'M. Shubbar', 'J. Vasquez', 'K. Somes', 'S. Chew', 'J. Washburn', 'P. Rai', 'J. Gipson', 'S. Smith'], 
['Ana Glaser', 'Y. S. Kunwar', 'A. Faltesek', 'C. Walenciak', 'T. Abera', 'J. Marin', 'C. Kim', 'P. Flaming', 'S. Fogelman', 'Y. Zhang', 'Y. Zhang', 'I. Nwaogu', 'A. Garapati', 'G. Lane', 'J. Gipson', 'M. Kuklani'],
 ['Jake Harrison', 'B. Dakshinamoorthi', 'A. Canton', 'T. Schwebke', 'A. Garapati', 'J. Gipson', 'A. Bravo', 'J. Washburn', 'A. Heroy', 'J. Pafford', 'A. Shen', 'D. Geislinger', 'J. Lancon', 'R. Djoko', 'H. Wang', 'B. Brewer'], 
['Juan Nunez', 'B. Kimbark', 'S. Smith', 'J.Villanueva', 'W. Arnost', 'M. Palanisamy', 'J.Tan', 'J. Coate', 'J.Villanueva', 'P. Attah', 'M. Weatherford', 'B. Arendale', 'S. Jung', 'S.n McWhirter', 'M. Kimari', 'C. Drake'], ['Neddy Nyatome', 'A. Thobani', 'Q. Chau', 'P. Flaming', 'J. Kassof', 'Balaji', 'J. Schueder', 'P. Leon', 'C. Nava', 'Balaji', 'T. Gianelle', 'J. Balson', 'D. Davieau', 'N. Rezsonya', 'B. Brewer', 'P. Leon'],
 ['Tina Pai', 'M. Pednekar', 'M. Garcia', 'B. Arendale', 'J. Saldana', 'D. Byrne', 'J. Rupp', 'J. Nguyen', 'N. Rezsonya', 'A. Siddiqui', 'N. Wittlin', 'S. Cocke', 'A. Bravo', 'A. Pathak', 'S. Mylapore', 'A. Thobani'], 
['Venkata Leela Maruthi Ganesh Vanga', 'W. Lai', 'A. Norman', 'T. Deason', 'N. Wall', 'K. Thomas', 'A. Nelson', 'M. Shulyk', 'B. Brewer', 'C. Martinez', 'K. Mendonsa', 'T. Gianelle', 'A. Pathak', 'S. Fogelman', 'M. Moro', 'J. Munguia'],
 ['Renfeng Wang', 'S. Zaheri', 'J. Lancon', 'K. Somes', 'N. Brown', 'S.n McWhirter', 'E. Carrera', 'T. Schwebke', 'Balaji', 'B. Stephan', 'A. Rajan', 'A. Roderick', 'B. Arendale', 'M. Kuklani', 'S.Gozdzialski', 'T. Prasad'], 
['Zachary Zaiken', 'B.  Franklin', 'J.Villanueva', 'P. Leon', 'J. Pafford', 'A. Schams', 'J. Harding', 'S. Mylapore', 'S. Daggubati', 'S. Prabhala', 'S. Fite', 'V. Viswanathan', 'P. Leon', 'A. Burnett', 'R. Chandna', 'S. Gu']]

Returned ranking:

# 1. Is this Fair?
# 2. Is this Efficient(human, computer)?
# 3. Do you trust your classmates?
# 4. How can we evaluate your classmates?
# 5. What assumptions go into this result?
# 6. Under what conditions would it fail?
# 7. How can we make it better?
######
# 8. Who is most likely to win given the above situation?
# 9. Who will have the fairest evaluation?
# 10. Who has the least fair evaluation?
# 11. Should we think equally about the first places as we thinking about the last places?

PUT YOUR REORDERED LIST OF RANKINGS BELOW:

[['Balasubramaniam Dakshinamoorthi', 'Arnost, William', 'J. Heinen', 'M. Toolin', 'R. Bss', 'R. Hazell', 'S. Daggubati', 'D.Stroud', 'J. Munguia  ', 'B. Kimbark', 'J. Knowles', 'N. Wittlin', 'Mathew, Lijju', 'G. Lane', 'N. Gupta', 'Vankina, Aniketh'],
 ['Christopher Dawson', 'T. Abera', 'S. Mylapore', 'J. Lin', 'B. Lee', 'Y. Leung', 'M. Rega', 'Y. Leung', 'N. Rezsonya', 'M. Garcia', 'A. Nelson', 'M. Luzardo', 'L. Sterling', 'K. Thomas', 'P. Leon', 'A. Veluchamy'], 
['Neha Dixit', 'M. Pednekar', 'Ghaemmaghami, Aurian', 'L. Sterling', 'B. Arendale', 'L. Zheng', 'M. Ludlow', 'K. Patterson', 'S. Hayden', 'Dhillon, Indy', 'R. Talk', 'J. Coate', 'J.Tan', 'B.Waite', 'S. Cocke', 'B. Arendale'], 
['Bodie Franklin', 'Stacy, Jules', 'A. Mohan', 'J. Coate', 'M. Rega', 'Clark, Daniel', 'Arnost, William', 'N. Wittlin', 'L. Cheng', 'B.Waite', 'J.Tan', 'K. Dickens', 'N. Wittlin', 'R. Hazell', 'Ibrahim, Daanesh', 'Ghaemmaghami, Aurian'],
 ['Kris Ghimire', 'M. Toolin', 'D. Shaw', 'D. Kunupudi', 'R. Nagarajan', 'J. Howard', 'Zhang, Yusi', 'D. Shaw', 'Dhillon, Indy', 'Ibrahim, Daanesh', 'M. Shubbar', 'Larsen, Andrew', 'H. Nguyen', 'A. Subramanian', 'A. Rajan', 'Crouthamel, Daniel'], 
['Walter Lai', 'N. Wall', 'A. Mejia', 'P. Adams', 'M. Ludlow', 'E. Carrera', 'S. Fite', 'J. Balson', 'Eysenbach, Joshua', 'S. Pillay', 'Ghaemmaghami, Aurian', 'A. Saxena', 'R. Simhambhatla', 'S. Kennedy', 'J. Lingle', 'S. Daggubati'],
 ['Samuel Onalaja', 'J. Vasquez', 'K. Okiah', 'Schueder, Joseph', 'S. Godbole', 'S. Hayden', 'M. J. Wolfe', 'S. Smith', 'B.Waite', 'R. Bss', 'Nguyen, Jeff', 'Mathew, Lijju', 'Washburn, Jeff', 'A. Siddiqui', 'R. Hazell', 'M. Ludlow'], 
['Jon Paugh', 'F. Poon', 'C. Nava', 'N. Wittlin', 'B. Kimbark', 'Philip ', 'Bracy, Dustin', 'K. Patterson', 'C. Drake', 'D. Davieau', 'L. Dajani', 'A. Cattley', 'A. Faltesek', 'B. Wilke', 'Vankina, Aniketh', 'G. Hudgeons'], 
['Kenneth Poling', 'V. Torres', 'P. Adams', 'S. Zaheri', 'C. Drake', 'K. Pradeepkumar', 'T. Gianelle', 'A. Saxena', 'Larsen, Andrew', 'K. Okiah', 'A. Ho', 'M. Rega', 'Prabhala, Sreeni', 'Prabhala, Sreeni', 'M. Kuklani', 'N. Wittlin'], ['Sabrina Purvis', 'M. Luzardo', 'S. Milett', 'Swenson, Paul', 'Mathew, Lijju', 'A. Veluchamy', 'Y. Zhang', 'J. Coate', 'A. Ansari', 'Savorgnan, Fabio', 'A. Bravo', 'M. Ludlow', 'S. Garcia de Alford', 'E. Fry', 'C. Drake', 'R. Nagarajan'], 
['Rajesh Satluri', 'D. Byrne', 'M. Garcia', 'S. Pillay', 'B. Stephan', 'C. Morgan', 'A. Burnett', 'J. Howard', 'J. Balson', 'B.Waite', 'J.Tan', 'J. Roach', 'B. Houssaye ', 'M. Shubbar', 'Nayden, Billy', 'K. Rollins'],
 ['Thad Schwebke', 'R. Djoko', 'P. Byrd', 'T. Pompo', 'Kaniti, Vijay', 'W. Trevino', 'M. Ludlow', 'S. Daggubati', 'W. Trevino', 'Kaniti, Vijay', 'A. Mohan', 'S. Cocke', 'Kaniti, Vijay', 'N. Brown', 'S. Garcia de Alford', 'S. Mylapore'], 
['Yucheol Shin', 'B.A. Kannan', 'A. Wilkins', 'A. Ruthford', 'G. Hudgeons', 'C. Hu', 'I. Bakhtiar', 'P. Byrd', 'N. Gupta', 'Y. Leung', 'R. Djoko', 'Lull, Ellen', 'R. Djoko', 'A. Ansari', 'Vela, Armando', 'Schueder, Joseph'],
 ['Jamie Vo', 'W. Trevino', 'A. Saxena', 'A. Ho', 'R. Djoko', 'R. Talk', 'J. Gipson', 'C. Walenciak', 'A. Nelson', 'Philip ', 'L. Clinton', 'S. Garcia de Alford', 'S. Mylapore', 'J. Balson', 'Y. Leung', 'S. Samuel'], 
['Michael Weatherford', 'K. Mendonsa', 'Zhang, Yusi', 'Schueder, Joseph', 'C. Martinez', 'M. Pednekar', 'C. Hu', 'J. Marin', 'S. Mylapore', 'Kaniti, Vijay', 'D. Julovich', 'A. Ruthford', 'R. Hazell', 'J. Lancon', 'P. Flaming', 'S. Fogelman'],
 ['Patricia Attah', 'A. Shen', 'G. Lane', 'M. Toolin', 'L. Cheng', 'B. Stephan', 'J. Partee', 'J. Lubich', 'M. Shubbar', 'R. Chandna', 'D. Josephs', 'Brionez, Jacob', 'D. Geislinger', 'T. Deason', 'C. Drake', 'J. Munguia  '], 
['Adam Canton', 'R. Meagher', 'M. Ludlow', 'Roderick, Allison', 'Pengilly, Thomas', 'S.Gozdzialski', 'R. Chandna', 'Kimari, Muchigi', 'D.Stroud', 'C. Graves', 'R. Bss', 'M. Toolin', 'B.A. Kannan', 'R. Hazell', 'K. Mendonsa', 'J. Lubich'], 
['Quynh Chau', 'A. Ho', 'V. Torres', 'K. Thomas', 'R. Quincy Paul', 'A. Siddiqui', 'J. Balson', 'P. Byrd', 'A. Ansari', 'J.Tan', 'S. Daggubati', 'Rai, Paritosh', 'C. Drake', 'J.Tan', 'Mathew, Lijju', 'Y. Zhang'],
 ['Dhruba Dey', 'B. Houssaye ', 'A. Subramanian', 'P. Flaming', 'J. Lin', 'K. Rollins', 'R. Simhambhatla', 'B.A. Kannan', 'Pengilly, Thomas', 'P. Kumar', 'Nelson, Morgan', 'T. Pompo', 'G. Kodi', 'D. Josephs', 'M. Shahini', 'Crouthamel, Daniel'], 
['Paul Huggins', 'J. Heinen', 'B.Waite', 'Roderick, Allison', 'Pengilly, Thomas', 'J. Au', 'A. Ho', 'C. Martinez', 'S. Fogelman', 'J. Saldana', 'C. Henderson', 'S. Hayden', 'Crouthamel, Daniel', 'N. Wittlin', 'P. Leon', 'Y. S. Kunwar'], 
['Gautam Kapila', 'Philip ', 'C. Hu', 'E. Carrera', 'H. Wang', 'Dhillon, Indy', 'B. Coari', 'J. Harding', 'K. Dickens', 'L. Clinton', 'R. Quincy Paul', 'A. Schams', 'Vankina, Aniketh', 'S. Chew', 'A. Bravo', 'A. Rajan'], 
['Julia Layne', 'B. Kimbark', 'P. Adams', 'A. Heroy', 'N. Wittlin', 'S. Jung', 'J. Knowles', 'M. Toolin', ' B. Benefield', 'L. Zheng', ' B. Benefield', 'M. Pednekar', 'Y. Chu', 'A. Mejia', 'Chinchilla, Matthew', 'Ibrahim, Daanesh'], 
['Rudranil Mitra', 'P. Kumar', 'Y. S. Kunwar', 'J.Tan', 'T. Gianelle', 'Swarupananda, Sid', 'Bracy, Dustin', 'Nayden, Billy', 'J. Balson', 'A. Subramanian', 'M. Hightower', 'A. Wilkins', 'S. Smith', 'A. Subramanian', 'S. Kennedy', 'V. Ahir'], 
['Suchismita Moharana', 'P. Kumar', 'Nelson, Morgan', 'T. Gianelle', 'J. Heinen', 'S. Jung', 'A. Ho', 'Zhang, Yusi', 'B. Stephan', 'Nguyen, Jeff', 'Brionez, Jacob', 'M. J. Wolfe', 'B. Kimbark', 'Lull, Ellen', 'M. Riley', 'F. A. Yeboah'], 
['Jason Rupp', 'A. Veluchamy', 'B. Arendale', 'G. Hudgeons', 'T. Abera', 'S. Smith', 'T. Prasad', 'S. Zaheri', 'A. Subramanian', 'A. Bravo', 'Y. Chu', 'L. Sterling', 'A. Siddiqui', 'A. Saxena', 'V. Ahir', 'R. Meagher'],
 ['Akbar Thobani', 'Mathew, Lijju', 'K. Rollins', 'J. Balson', 'A. Cattley', 'S. Milett', 'Rai, Paritosh', 'Swarupananda, Sid', 'S. Cocke', 'S. Smith', 'A. Rajan', 'S.t Miller', 'B. Brewer', 'J. Lancon', 'C. Hu', 'R. Hazell'], ['Bosang Yun', 'B. Houssaye ', 'K. Rollins', 'C. Morgan', 'K. Somes', 'T. Pompo', 'K. Patterson', 'Prabhala, Sreeni', 'A. Veluchamy', 'D. Kunupudi', 'S. Samuel', 'B.Waite', 'S. Zaheri', 'J. Howard', 'Rai, Paritosh', 'S.n McWhirter']]

# For next week please return a list with your name and the rankings of the
# videos from first to last EXACTLY as they are above.  

# Summer 2021 CLASS INSERT RANKINGS BELOW HERE↓↓↓↓↓↓↓ 
(In List format ranking Best → Worst)

[['Balasubramaniam Dakshinamoorthi', 'Arnost, William',  'N. Gupta', 'J. Knowles','Vankina, Aniketh', 'G. Lane','J. Heinen', 'M. Toolin', 'R. Bss', 'R. Hazell', , 'D.Stroud', 'J. Munguia  ', 'B. Kimbark', 'N. Wittlin', 'Mathew, Lijju','B.A..Kannan'],
['Bodie Franklin','M. Rega','Ghaemmaghami, Aurian','Arnost, William','B.Waite','Ibrahim, Daanesh','Stacy, Jules','R. Hazell','N. Wittlin','J. Coate','K. Dickens','Clark, Daniel','J.Tan','L. Cheng','N. Wittlin','A. Mohan'],
['Gautam Kapila', 'B. Coari', 'J. Harding','K. Dickens', 'Dhillon, Indy',  'H. Wang', 'L. Clinton', 'A. Bravo', 'Vankina, Aniketh','C. Hu',  'R. Quincy Paul', 'Philip ', 'E. Carrera', 'A. Schams', 'S. Chew', 'A. Rajan'], 
['Paul Huggins', 'Crouthamel, Daniel','Pengilly, Thomas','J. Heinen','J. Au','J. Saldana','S. Hayden','B.Waite','Roderick, Allison','A. Ho','C. Martinez','S. Fogelman','C. Henderson','N. Wittlin','P. Leon','Y. S. Kunwar'],
['Christopher Dawosn', 'M. Garcia', 'A. Nelson', 'B. Lee', 'J. Lin', 'L. Sterling', 'M. Luzardo', 'Y. Leung', 'K. Thomas', 'S. Mylapore', 'P. Leon', 'M. Rega', 'N. Rezsonya', 'T. Abera', 'A. Veluchamy'],
['Sabrina Purvis', 'R. Nagarajan', 'Mathew, Lijju', 'Y. Zhang', 'J. Coate', 'M. Luzardo', 'M. Ludlow', 'S. Garcia de Alford', 'A. Bravo', 'Savorgnan, Fabio', 'A. Ansari', 'A. Veluchamy', 'S. Milett', 'E. Fry', 'C. Drake', 'Swenson, Paul'],
['Rajesh Satluri', 'B. Houssaye', 'J. Roach', 'C. Morgan', 'M. Garcia', 'J. Howard', 'J. Balson', 'S. Pillay', 'B. Stephan', 'K. Rollins', 'M. Shubbar', 'D. Byrne', 'A. Burnett', 'J.Tan', 'B.Waite', 'Nayden, Billy']
['Thad Schwebke', 'N. Brown','S. Cocke','J. Partee','M. Ludlow','S. Mylapore','B. Lee','A. Mohan','P. Byrd','Y. Leung','S. Garcia de Alford','W. Trevino','K. Patterson','T. Pompo','Kaniti, Vijay','R. Djoko','S. Daggubati']
['Julia Layne', 'S. Jung', 'B. Kimbark', 'M. Toolin', 'N. Wittlin', 'S. Mylapore', ' B. Benefield', 'M. Pednekar', 'Y. Chu', 'L. Zheng', 'A. Heroy', 'Chinchilla, Matthew', 'Ibrahim, Daanesh', 'A. Mejia',  'P. Adams', 'J. Knowles'], 

['Bosang Yun', 'K. Somes','J. Howard','B.Waite', 'B. Houssaye', 'K. Patterson','Rai, Paritosh','A. Veluchamy','S.n McWhirter',  'K. Rollins', 'Prabhala, Sreeni',  'C. Morgan', 'T. Pompo',  'D. Kunupudi',  'S. Samuel', 'S. Zaheri']

['Jon Paugh',  'G. Hudgeons', 'A. Cattley', 'Bracy, Dustin', 'Vankina, Aniketh', 'A. Faltesek', 'C. Nava', 'L. Dajani', 'F. Poon','Philip ', 'N. Wittlin','B. Kimbark', 'K. Patterson', 'C. Drake', 'D. Davieau',  'B. Wilke' ], 
['Neha Dixit','B.Waite', 'J.Tan', 'B. Arendale','S. Cocke', 'J. Coate','R. Talk', 'Dhillon, Indy', 'S.Hayden', 'K. Patterson','M. Ludlow','Ghaemmaghami, Aurian','B. Arendale','M. Pednekar','L. Sterling','L. Zheng']
['Jamie Vo' , 'J. Balson' , 'A. Saxena' , 'A. Ho' , 'L. Clinton' , 'A. Nelson' , 'S. Garcia de Alford' , 'S. Samuel' , 'S. Mylapore' , 'J. Gipson' , 'R. Talk' , 'Y. Leung' , 'W. Trevino' , 'R. Djoko'  , 'Philip ', 'C. Walenciak']
['Yucheol Shin',  'Vela, Armando', 'A. Wilkins', 'Schueder, Joseph', 'G. Hudgeons', 'A. Ansari',  'P. Byrd', 'B.A. Kannan', 'N. Gupta', 'Lull, Ellen', 'Y. Leung', 'R. Djoko', 'I. Bakhtiar','C. Hu', 'A. Ruthford'] 

 ['Jason Rupp', 'G. Hudgeons', 'A. Saxena', 'A. Siddiqui', 'V. Ahir', 'A. Bravo', 'Y. Chu', 'T. Abera', 'A. Subramanian', 'R. Meagher', 'T. Prasad', 'A. Veluchamy', 'B. Arendale',  'L. Sterling', 'S. Smith', 'S. Zaheri']
['Michael Weatherford', 'A. Ruthford', 'C. Martinez', 'M. Pednekar', 'S. Fogelman', 'J. Lancon', 'K. Mendonsa', 'Zhang, Yusi', 'R. Hazell', 'P. Flaming', 'Schueder, Joseph', 'J. Marin', 'Kaniti, Vijay', 'D. Julovich', 'S. Mylapore', 'C. Hu']
['Patricia Attah','M. Shubbar', 'G. Lane', 'A. Shen', 'M. Toolin','B. Stephan',  'R. Chandna',  'J. Partee', 'J. Lubich','L. Cheng','T. Deason', 'D. Josephs','Brionez, Jacob', 'D. Geislinger', 'C. Drake', 'J. Munguia  ']

 ['Adam Canton', 'K. Mendonsa', 'T. Pengilly', 'R. Chandna', 'D.Stroud', 'C. Graves', 'R. Bss', 'B.A. Kannan', 'R. Meagher', 'M. Ludlow', 'M. Toolin', 'S.Gozdzialski', 'R. Hazell', 'J. Lubich', 'K. Muchigi', 'Roderick, Allison']'

['Walter Lai', 'A. Saxena', 'M. Ludlow','P Adams','S Fite','A Ghaemmaghami','N Wall','J Balson','J Eysenbach','J Lingle', 'S. Pillay','R. Simhambhatla', 'S. Kennedy',  'A. Mejias','E Carrera','S. Daggubati']

['Suchismita Moharana', 'Nelson, Morgan',  'B. Kimbark', 'S.t Miller', 'A. Heroy',  'A. Ho', 'M. Riley',  'T. Gianelle', 'M. J. Wolfe', 'K. Rollins', 'Nguyen, Jeff', 'B. Stephan',  'Zhang, Yusi', 'J. Heinen', 'S. Jung',  'P. Kumar',  'Lull, Ellen',  'F. A. Yeboah', 'Brionez, Jacob'], 

['Kenneth Poling', 'Larsen, Andrew', 'T. Gianelle', 'K. Okiah', 'W. Arnost',  'M. Rega', 'A. Ho', 'A. Saxena', 'N. Wittlin', 'P. Adams', 'M. Kuklani', 'K. Pradeepkumar', 'Prabhala, Sreeni', 'C. Drake', 'V. Torres', 'S. Zaheri'], 

 ['Samuel Onalaja', 'B.Waite',  'J. Vasquez', 'K. Okiah', 'Schueder, Joseph', 'S. Godbole', 'S. Hayden', 'M. J. Wolfe', 'S. Smith', 'R. Bss', 'Nguyen, Jeff', 'Mathew, Lijju', 'Washburn, Jeff', 'A. Siddiqui', 'R. Hazell', 'M. Ludlow'],

['Rudranil Mitra', 'T. Gianelle', 'Bracy, Dustin', 'J. Balson', 'A. Subramanian', 'M. Hightower', 'S. Smith', 'A. Subramanian', 'S. Kennedy', 'V. Ahir','A. Wilkins', 'P. Kumar', 'Y. S. Kunwar', 'Nayden, Billy','J.Tan','Swarupananda, Sid'],


Returned ranking:
# 1. Is this Fair?
# 2. Is this Efficient(human, computer)?
# 3. Do you trust your classmates?
# 4. How can we evaluate your classmates?
# 5. What assumptions go into this result?
# 6. Under what conditions would it fail?
# 7. How can we make it better?
######
# 8. Who is most likely to win given the above situation?
# 9. Who will have the fairest evaluation?
# 10. Who has the least fair evaluation?
# 11. Should we think equally about the first places as we thinking about the last places?

 ['Akbar Thobani', 'Mathew, Lijju', 'K. Rollins', 'J. Balson', 'A. Cattley', 'S. Milett', 'Rai, Paritosh', 'Swarupananda, Sid', 'S. Cocke', 'S. Smith', 'A. Rajan', 'S.t Miller', 'B. Brewer', 'J. Lancon', 'C. Hu', 'R. Hazell'],

Returned Ranking:
Ranking
Presenter
Presentation Description
1
A. Cattley
Advanced Loss Functions
2
K. Rollins
Gradient Descent Optimization Algorithms
3
B. Brewer
Generative Adversarial Networks
4
 L. Mathew
Models for web search
5
R. Hazell
Connecting the Beta and Binomial Distribution with Bayes' Theorem
6
Rai, Paritosh
Understanding Back Propagation Neural Network
7
J. Balson
On the shortest spanning subtree of a graph and the traveling salesman problem
8
S.t Miller
Bidirectional Sequence Models
9
S. Milett
Image denoising using Autoencoders
10
S. Smith
Quantization of Neural Networks
11
C. Hu
Few shot learning with memory-augmented NN

 ['Kris Ghimire', 'M. Toolin',  'Zhang  Yusi', 'Crouthamel, Daniel','J. Howard', 'Ibrahim, Daanesh', 'Dhillon, Indy', 'D. Shaw', 'H. Nguyen' , 'A. Subramanian', 'D. Kunupudi', , 'M. Shubbar', 'A. Rajan',, , 'R. Nagarajan', 'Larsen, Andrew'], 

['Quynh Chau', 'A. Ho',  'Mathew, Lijju', 'B. Houssaye', 'R. Quincy Paul', 'Rai, Paritosh', 'A. Ansari', 'A. Siddiqui', 'K. Thomas', 'J. Balson', 'Y. Zhang', 'J.Tan', 'Y. Zhang', 'S. Daggubati',  'A. Siddiqui', 'C. Drake']

import pdb; pdb.set_trace()

#Winter2021 Class rankings below ( not sure where to put them Santerre) -- AH

['Bhaumik, Mrinmoy', 'J. Howard', 'L. Clinton', 'J. Lubich', 'S. Garcia de Alford', 'J. Vasquez', 'A. Garapati', 'G. Kodi', 'M. Luzardo', 'S. Fogelman', 'B.A. Kannan']
['Clark, Daniel  'S.t Miller', ',B. Arendale',  'G. Lane',  'M. Shulyk', 'K. Thomas','J. Knowles', 'M. Rega', 'J. Lancon    ', ' 'F. Poon', 'N. Gupta'], 
['Roderick, Allison', 'R. Talk', 'R. Hazell', 'K. Rollins', 'Y. Zhang', 'A. Shen', 'J.Villanueva', 'S. Cocke', 'K. Thomas', 'C. Walenciak', 'V. Torres'], 
['Schueder, Joseph',  'B. Brewer',  'A. Burnett', 'Y. Leung' ,'S. Jung', 'A. Bravo', 'B. Houssaye ' ,'D. Davieau', 'L. Jiang','T. Prasad', 'F. A. Yeboah'],
['Rai, Paritosh', 'A. Nelson', 'J. Harding', 'A. Saxena, 'G Kodi', 'T. Deason', 'T. Prasad', 'H. Wang', 'A. Faltesek', 'A. Mejia', 'S. Garcia de Alford', 'S. Daggubati']
['Larsen, Andrew', 'S. Sprague', 'A. Wilkins', 'L. Dajani', 'M. Moro', 'D. Davieau', 'M. Garcia', 'S. Chew', 'S. Samuel', 'M. Ludlow', 'R. McDaniel']
['Nelson, Morgan','T. Pompo','A. Saxena','I. Bakhtiar','S. Milett','K. Patterson','B.Waite','M. Shahini','J.Villanueva','A. Rajan','M. Riley'],
['Kimari, Muchigi', 'N. Brown',' B. Benefield', 'J. Knowles', 'G. Lane', 'R. Talk', 'T. Deason', 'K. Rollins', 'B. Stephan', 'J. Lubich','R. Djoko'] 
['Kaniti, Vijay','R. Quincy Paul','J. Partee','J. Howard','F. Poon','S.t Miller','T. Prasad','S. Pillay', 'B. Benefield', 'A. Burnett','S.Gozdzialski']
['Chinchilla, Matthew', 'B. Kimbark',  'S. Smith', 'K. Chang', 'N. Rezsonya', 'H. Nguyen', 'A. Bravo',  'A. Ansari', 'A. Ruthford','C. Walenciak'], 
['Nguyen, Jeff', 'C. Nava', 'H. Nguyen', 'A. Faltesek', 'Y. Chu', 'K. Somes', 'K. Somes', 'J. Flores', 'S. Mylapore', 'F. A. Yeboah', 'K. Chang'],
['Washburn, Jeff', 'A. Faltesek', 'D.Stroud', 'A. Bravo', 'F. Poon', 'A. Garapati', 'E. Carrera', 'D. Davieau', 'T. Pompo', 'T. Prasad', 'A. Ruthford'], 
['Ibrahim, Daanesh', 'S. Sprague', 'D.Stroud', 'S. Pillay', 'S. Jung',  'H. Nguyen', 'A. Saxena', 'N. Gupta', 'M. Pednekar', 'S. Zaheri', 'Y. S. Kunwar'], 
['Bourzikas, Grant', 'Y. Zhang', 'N. Wittlin', 'J. Marin', 'D. Josephs', 'N. Gupta', 'J. Lubich', 'I. Bakhtiar', 'P. Leon', 'M. Moro', 'A. Mejia'],
['Vankina, Aniketh', 'J. Kassof', 'P. Adams', 'R. Quincy Paul', 'A. Norman ', 'B. Stephan', 'J. Saldana', 'J. Tan', 'W.Trevino', 'A. Subramanian', 'F.A. Yeboah'],
['Crouthamel, Daniel', 'C. Hu', 'J. Lubich', 'M. Moro', 'J. Heinen', 'J. Au', 'J. Pafford', 'B. Wilke', 'M. Toolin', 'S. Zaheri', 'J. Lancon    '],
['Ghaemmaghami, Aurian', 'R. Talk', 'R. Hazell', 'M. Moro', 'Y. Zhang', 'Z. Gill', 'K. Dickens', 'S. Godbole', 'J. Lingle', 'Y. S. Kunwar', 'J. Munguia']
['Vela, Armando', 'M. J. Wolfe', 'R. Quincy Paul', 'Z. Gill', 'B. Wilke', 'M. Moro', 'A. Cattley', 'V. Viswanathan', 'A. Siddiqui', 'A. Subramanian', 'V. Torres'],
['Lull, Ellen', 'R. Hazell',  'S. Mylapore',  'M. Kuklani' , 'P. Adams', 'T. Pompo', 'N. Wall', 'Y. Chu', 'M. Pednekar', 'Y. Zhang'],
['Dhillon, Indy', 'J. Roach', 'D. Josephs', 'G. Hudgeons', 'K. Dickens', 'C. Nava',  'A. Bravo', 'K. Somes', 'T. Deason', 'S. Chavan', 'J. Vasquez'],  
['Prabhala, Sreeni',  'J. Howard', 'K. Okiah', 'K. Ayala', 'J. Partee', 'J.Villanueva', 'B. Lee', 'Philip ', 'A. Garapati', 'P. Kumar', 'P. Flaming'],
['Eysenbach, Joshua', 'M. Hightower',  ' B. Benefield',  'N. Wittlin',  'S. Godbole',  'S. Cocke',  'F. Poon',  'Y. Leung',  'A. Ruthford',  'S. Daggubati',   'Y. S. Kunwar'], 
['Zhang, Yusi',  'D.Stroud','F, Poon', 'J. Heinen', 'A. Wilkins', 'C. Walenciak', 'D. Davieau', 'D. Julovich', 'V. Ahir', 'E. Carrera', 'L. Jiang'],
['Stacy, Jules', 'A. Saxena',  'A. Wilkins', ' B. Benefield',  'J. Lancon    ', 'T. Deason', 'J. Heinen', 'S. Godbole', 'Y. Chu', 'B. Arendale', 'H. Nguyen'], 

# CLASS 1 CURRENT SEMESTER SUMMER 2020

['Waite, Brian','M. Shulyk','K. Dickens','T. Deason','D. Josephs','K. Thomas','N. Brown','J. Knowles','F. A. Yeboah']
['Walenciak, Carl', 'B. Benefield', 'B.A. Kannan', 'S. Hayden', 'R. Nagarajan', 'J. Gipson, 'W. Trevino', 'S. Merrit',  'J. Yi'], 
['Fry, Edward', 'L. Jiang', 'B. Benefield', 'D. Geislinger', 'L. Cheng', 'M. Palanisamy', 'Yat Leung', 'L. Zheng', 'J. Flores']
['Tan, Jonathan',' P.Byrd', 'B.Wilke', 'M.Toolin', 'B.A.Kannan', 'J.Pafford', 'S.Daggubati', 'J.Au', 'P.Flaming']
['Faltesek, Aaron', 'J. Lancon', 'D.Stroud', 'M. J. Wolfe', 'T. Deason', 'E. Carrera', 'A. Nguyen', 'M. Toolin', 'V. Ahir']
['Gianelle, Tom', 'J. Saldana', 'J. Marin', 'D. Davieau', 'M. Shulyk', 'M. J. Wolfe', 'M. Shahini', 'R. Cha ndna', 'C. Drake'], 
['Rodgers, John', 'D. Geislinger', 'R. Chandna', 'B.A. Kannan', 'G. Lane', 'L. Jiang', 'J. Gipson', 'D. Byrne', 'S. Merrit'],
['Thompson, Kevin', 'T. Deason', 'L. Sterling', 'J. Munguia', 'A. Ho', 'R. Bss', 'B.A. Kannan', 'Y. Chu']
['Behuria Pathak, Amita', 'J. Gipson', 'J. Lin', 'B. Houssaye ', 'S. Godbole', 'S. Hayden', 'J.Villanueva', 'A. Wilkins', 'J. Saldana']
['Nielsen, Heber', 'J. Gipson', 'B. Wilke', 'A. Saxena', 'T. Deason', 'G. Lane',  'K. Somes', 'M. J. Wolfe', 'J. Vasquez', 'A. Cattley]
['Mansor, Maysam', 'A. Mohan',  'K. Somes', 'P. Flaming', 'C. Drake', 'R. Simhambhatla', 'R. Bss', 'K. Okiah']

# CLASS 2 CURRENT SEMESTER SUMMER 2020

['Croom, Brandon', 'D. Josephs',  'N. Gupta', 'M. Hightower', 'M. Toolin', 'R. Simhambhatla', 'S. Chew', 'J. Flores', 'D. Davieau'],
['Kumar, Pradeep',  'A. Saxena', 'J. Partee' ,'C. Graves',  'P. Byrd', 'S. Gu', 'V. Ahir','M. Shahini', 'S. Mylapore', ], 
['Shaw, David', 'B.A. Kannan', 'B. Arendale', 'S. Godbole', 'A. Ho', 'M. Ludlow', 'S. Gu', 'J. Marin', 'J. Pafford']
['Jung, Shawn Jonghyuck','A. Rajan', 'D. Byrne',  'A. Wilkins', 'C. Hu', 'K. Okiah', 'B. Wilke', 'S.Gozdzialski', 'A. Mohan']
['Burnett, Amber', 'B. Kimbark', 'A. Garapati', 'L. Sterling', 'K. Okiah', 'M. Toolin', 'B. Yu', 'P. Flaming', W. Trevino'],
['Clinton, Laurence','Z. Gill','J. Kassof','C. Morgan','S. Gu','D. Josephs', 'R. Bss','N. Rezsonya','Yat Leung'],
['Howard, Justin','J. Heinen', 'K. Mendonsa', 'A. Ansari', 'M. Hightower',  'M. Rega', 'P. Leon', 'T. Pompo'],
['Harding, James','N. Brown', 'A. Nguyen', 'M. Shubbar', 'A. Nelson', 'S. Godbole','L. Sterling', 'J. Lancon', 'C. Henderson'],
['Caguioa, Joseph', 'A. Ho', 'R. Hazell', 'S. Cocke', 'E. Carrera', 'C. Martinez', 'M. Garcia', 'M. Hightower', 'J. Yi']
['Djoko, Rikel',  'B. Houssaye ',  'G. Kodi',  'A. Nelson','P. Leon',  'L. Sterling',  'A. Wilkins',  'D. Josephs', 'B. Arendale']



 


























LAST CLASSES JUDGMENTS
### please place judgments here
['Paul, Ryan Quincy', 'N. Wittlin', 'B. Yu', 'K. Dickens', 'J. Heinen', 'A. Subramanian', 'C. Hu']
['Kumar, Pankaj', 'S. Mylapore', 'J. Gipson', 'S. Samuel' , 'T. Deason' , 'J. Saldana', 'B.A. Kannan']
['Lee, Bruce', 'J. Heinen', 'J. Pafford', 'S. Hayden', 'J.Villanueva', 'V. Viswanathan', 'T. Deason']
['Partee, John', 'B.A. Kannan','J. Saldana',  'M. Hightower', 'A. Subramanian', 'J. Knowles', 'M. Pednekar'], 
['Coleman, Jasmine', 'K. Okiah', 'A. Mohan', 'M. Pednekar', 'J.Villanueva', 'K. Dickens', 'J. Yi'],
['Nguyen, Andy', 'N. Brown', 'R. Bss', 'R. Bss', 'M. Shulyk', 'G. Lane', 'P. Flaming'],
['Fogelman, Spencer', 'R. Simhambhatla', 'C. Morgan','J.Villanueva','P. Leon' ,'K. Dickens', 'S. Daggubati'],
['Wolfe, Michael',  'S. Samuel', 'N. Wall', 'G. Lane', 'S. Mylapore', 'P. Flaming', 'C. Drake'],
['Rajan, Anand', 'A.ho','T.Deason','A.Nelson','J.Lingle', 'K.Thomas', 'T.Pompo'],
['Heroy, Andrew', 'T. Deason', 'S. Mylapore', 'C. Kim', 'J. Knowles', 'D. Davieau',  'T. Pompo'] 
['Hudgeons, Gavin', 'D. Davieau', 'B.A. Kannan', 'C. Hu', 'A. Veluchamy', 'M. Palanisamy', 'S. Milett']
['HENDERSON, CHARLES',  'A. Shen', 'S. Cocke', 'S. Cocke', 'J. Saldana', 'L. Cheng', 'F. A. Yeboah']
['Jurek, Karl',  'J. Flores', 'M. Palanisamy', 'R. Simhambhatla',  'A. Subramanian',  'S. Loftin', 'J. Vasquez',]
['Hazell, Robert',  'Z. Gill', 'D. Geislinger', 'D. Davieau', 'T. Deason',  'S. Chew',  'S. Loftin']
['Chandna, Rajat', 'K. Thomas', 'M. Rega', 'M. Toolin', 'M. Kuklani', 'L. Jiang', 'S. Hayden'], 
['Chang, Kevin',  'N. Wall', 'M. Hightower', 'K. Mendonsa', 'V. Viswanathan', 'S. Sprague', 'P. Leon']
['Kunupudi, Deepti', 'M. Shahini', 'M. Toolin','N. Gupta','D. Davieau','L. Cheng','S. Loftin']
['Leung, Yat', 'J. Au' , 'L. Sterling', 'C. Hu', 'E. Carrera', 'C. Hu','Y. S. Kunwar'], 
['Torres, Vanessa', 'K. Okiah', 'M. Shahini', 'A. Veluchamy', 'A. Siddiqui', 'V. Ahir', 'G. Kodi'],
['Huang, Liang', 'P. Flaming', 'N. Brown', 'J. Lin', 'S. Mylapore', 'A. Saxena', 'M. Shubbar'],
['Jiang, Joe', 'N. Gupta', 'A. Nelson' , 'T. Pompo', 'S. Hayden',  'V. Viswanathan', 'L. Cheng'],
['Brewer, Blaine', 'S. Samuel', 'Z. Gill', 'J. Lingle', 'A. Schams', 'J. Gipson', 'S. Loftin'], 
['Munguia, Joseph', 'K. Thomas','V. Viswanathan', 'S. Chew','S. Hayden', 'J. Heinen','M. Shulyk'],
['ANSARI, ALLEN', 'A. Shen',  'L. Dajani', 'N. Gupta','P. Byrd', 'B. Yu', 'S. Chew'],
['Godbole, Shantanu','Z. Gill', 'A. Shen' , 'L. Sterling' , 'B. Kimbark' , 'G. Lane' , 'P. Flaming'], 
 ['Zheng, Limin', 'J. He
[['Arnost, William', 'P. Adams', 'S. Godbole', 'G. Hudgeons', 'J. Harding', 'M. Pednekar', 'C. Kim', 'K. Chang', 'J.Tan', 'S. Fite', 'C. Drake'], ['Bhaumik, Mrinmoy', 'M. Luzardo', 'S. Fogelman', 'L. Clinton', 'G. Kodi', 'J. Howard', 'B.A. Kannan', 'J. Lubich', 'J. Vasquez', 'A. Garapati', 'S. Garcia de Alford'], ['Brionez, Jacob', 'S. Jung', 'R. Chandna', 'C. Morgan', 'J. Lubich', 'A. Shen', 'V. Ahir', 'E. Fry', 'J. Partee', 'M. Shulyk', 'M. Luzardo'], ['Crouthamel, Daniel', 'J. Lubich', 'C. Hu', 'J. Lancon    ', 'J. Pafford', 'J. Heinen', 'S. Zaheri', 'M. Toolin', 'J. Au', 'M. Moro', 'B. Wilke'], ['Eysenbach, Joshua', 'Y. S. Kunwar', 'S. Godbole', 'S. Cocke', ' B. Benefield', 'S. Daggubati', 'M. Hightower', 'A. Ruthford', 'N. Wittlin', 'Y. Leung', 'F. Poon'], ['Ghaemmaghami, Aurian', 'J. Lingle', 'Y. S. Kunwar', 'K. Dickens', 'R. Talk', 'R. Hazell', 'M. Moro', 'Z. Gill', 'S. Godbole', 'J. Munguia  ', 'Y. Zhang'], ['Ibrahim, Daanesh', 'S. Sprague', 'S. Zaheri', 'D.Stroud', 'S. Pillay', 'A. Saxena', 'Y. S. Kunwar', 'M. Pednekar', 'N. Gupta', 'S. Jung', 'H. Nguyen'], ['Lull, Ellen', 'N. Wall', 'M. Pednekar', 'S. Mylapore', 'N. Wall', 'M. Kuklani', 'P. Adams', 'T. Pompo', 'Y. Chu', 'R. Hazell', 'Y. Zhang'], ['Nayden, Billy', 'M. Garcia', 'A. Rajan', 'C. Kim', 'B.A. Kannan', 'J. Pafford', 'K. Somes', 'S. Garcia de Alford', 'N. Rezsonya', 'D. Josephs', 'S. Zaheri'], ['Nelson, Morgan', 'B.Waite', 'M. Riley', 'A. Rajan', 'I. Bakhtiar', 'S. Milett', 'T. Pompo', 'K. Patterson', 'A. Saxena', 'M. Shahini', 'J.Villanueva'], ['Nguyen, Jeff', 'K. Somes', 'J. Flores', 'S. Mylapore', 'F. A. Yeboah', 'K. Chang', 'A. Faltesek', 'C. Nava', 'H. Nguyen', 'Y. Chu', 'K. Somes'], ['Pengilly, Thomas', 'C. Kim', 'A. Ansari', 'C. Graves', 'C. Kim', 'J. Au', 'V. Ahir', 'N. Brown', 'R. Talk', 'H. Nguyen', 'K. Patterson'], ['Roderick, Allison', 'J.Villanueva', 'C. Walenciak', 'R. Hazell', 'Y. Zhang', 'S. Cocke', 'R. Talk', 'V. Torres', 'K. Thomas', 'K. Rollins', 'A. Shen'], ['Savorgnan, Fabio', 'J. Au', 'M. Toolin', 'A. Wilkins', 'C. Nava', 'Y. Leung', 'D. Byrne', 'J. Balson', 'E. Carrera', 'Y. Zhang', 'C. Kim'], ['Schueder, Joseph', 'A. Bravo', 'A. Burnett', 'S. Jung', 'Y. Leung', 'D. Davieau', 'L. Jiang', 'T. Prasad', 'B. Brewer', 'F. A. Yeboah', 'B. Houssaye '], ['Stacy, Jules', 'T. Deason', 'J. Heinen', 'S. Godbole', 'A. Wilkins', 'B. Arendale', ' B. Benefield', 'Y. Chu', 'H. Nguyen', 'J. Lancon    ', 'A. Saxena'], ['Swenson, Paul', 'B. Stephan', 'S. Daggubati', 'N. Wall', 'L. Dajani', 'V. Torres', 'L. Clinton', 'M. Riley', 'D. Shaw', 'S. Sprague', 'G. Hudgeons'], ['Vela, Armando', 'A. Siddiqui', 'Z. Gill', 'M. Moro', 'B. Wilke', 'V. Viswanathan', 'V. Torres', 'R. Quincy Paul', 'M. J. Wolfe', 'A. Subramanian', 'A. Cattley'], ['Washburn, Jeff', 'D.Stroud', 'T. Prasad', 'F. Poon', 'T. Pompo', 'A. Faltesek', 'D. Davieau', 'E. Carrera', 'A. Garapati', 'A. Bravo', 'A. Ruthford'], ['Zhang, Yusi', 'J. Heinen', 'D.Stroud', 'D. Davieau', 'A. Wilkins', 'V. Ahir', 'D. Julovich', 'F. Poon', 'E. Carrera', 'L. Jiang', 'C. Walenciak'], ['Avvaru, Balaji', 'D.Stroud', 'S. Fogelman', 'S. Milett', 'P. Adams', 'L. Cheng', 'J. Vasquez', 'L. Jiang', 'B. Kimbark', 'M. Ludlow', 'B. Wilke'], ['Bracy, Dustin', 'J. Marin', 'I. Bakhtiar', 'D. Josephs', 'N. Wittlin', 'M. Moro', 'P. Leon', 'J. Lubich', 'Y. Zhang', 'N. Gupta', 'A. Mejia'], ['Chinchilla, Matthew', 'A. Ruthford', 'H. Nguyen', 'S. Smith', 'N. Rezsonya', 'B. Kimbark', 'K. Chang', 'M. Palanisamy', 'A. Bravo', 'A. Ansari', 'C. Walenciak'], ['Clark, Daniel', 'K. Thomas', 'M. Shulyk', 'J. Lancon    ', 'B. Arendale', 'F. Poon', 'N. Gupta', 'S.t Miller', 'M. Rega', 'J. Knowles', 'G. Lane'], ['Dhillon, Indy', 'A. Bravo', 'J. Vasquez', 'J. Roach', 'K. Somes', 'G. Hudgeons', 'T. Deason', 'S. Chavan', 'C. Nava', 'D. Josephs', 'K. Dickens'], ['Gaither, Brian', 'A. Heroy', 'B. Kimbark', 'M. Toolin', 'B. Yu', 'N. Brown', 'J. Kassof', 'J. Marin', 'S. Zaheri', 'D.Stroud', 'A. Nelson'], ['Kaniti, Vijay', 'S. Pillay', 'S.Gozdzialski', 'R. Quincy Paul', 'F. Poon', 'J. Partee', 'T. Prasad', 'S.t Miller', 'J. Howard', ' B. Benefield', 'A. Burnett'], ['Kimari, Muchigi', 'G. Lane', 'J. Lubich', 'R. Talk', 'T. Deason', 'K. Rollins', ' B. Benefield', 'R. Djoko', 'B. Stephan', 'J. Knowles', 'N. Brown'], ['Larsen, Andrew', 'A. Wilkins', 'R. McDaniel', 'M. Garcia', 'A. Wilkins', 'L. Dajani', 'L. Dajani', 'M. Moro', 'S. Samuel', 'S. Chew', 'D. Davieau'], ['Mathew, Lijju', 'C. Drake', 'A. Bravo', 'R. Nagarajan', 'D. Shaw', 'B. Yu', 'J. Partee', 'M. Shahini', 'G. Kodi', 'L. Cheng', 'N. Gupta'], ['Prabhala, Sreeni', 'K. Ayala', 'P. Flaming', 'J. Howard', 'J.Villanueva', 'K. Okiah', 'Philip ', 'P. Kumar', 'J. Partee', 'P. Kumar', 'A. Garapati'], ['Rai, Paritosh', 'A. Faltesek', 'T. Prasad', 'T. Deason', 'S. Daggubati', 'S. Garcia de Alford', 'A. Mejia', 'H. Wang', 'G. Kodi', 'A. Saxena', 'J. Harding'], ['Swarupananda, Sid', 'C. Morgan', 'S. Zaheri', 'S. Garcia de Alford', 'S. Milett', 'A. Saxena', 'R. Meagher', 'B. Brewer', 'R. Hazell', 'T. Prasad', 'E. Carrera'], ['Vankina, Aniketh', 'F. A. Yeboah', 'J. Saldana', 'B. Stephan', 'R. Quincy Paul', 'A. Subramanian', 'J. Kassof', 'W. Trevino', 'A. Norman', 'P. Adams', 'J.Tan']]inen', 'J. Marin', 'C. Martinez', 'C. Martinez', 'S. Chew', 'R. Nagarajan'],
['Chu, Yongjun', 'R. Bss',  'B. Benefield', 'N. Rezsonya', 'S. Fite', 'P. Leon', 'S. Merrit' ], 
['Cattley, Aaron', 'B. Houssaye', 'R. Talk', 'R. Bss', 'A. Nelson', 'M. Moro', 'S. Zaheri'], 
['Harding, James', 'J. Heinen','A. Mohan','A. Mohan', 'N. Gupta', 'P. Flaming', 'C. Martinez', ], 
['Garapati,Aditya','K. Rollins','S.Gozdzialski','C. Drake','J. Heinen','S. Milett','S. Zaheri'], 
['Arendale, Brady', 'B. Coari', 'K. Okiah', 'G. Kodi', 'L. Dajani', 'S. Zaheri', 'J. Yi'],
['Somes, Karen', 'S. Chew', 'Z. Gill,' 'R. Bss', 'K. Mendonsa', 'M. Luzardo', 'K. Thomas'],

['Norman, Alexandra', 'S. Gu', 'T. P


ompo', 'C. Morgan', 'S. Hayden', 'T. Prasad',  'C. Drake'],



