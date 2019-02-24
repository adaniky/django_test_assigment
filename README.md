## Task is to develop a web-based Employee Directory.
### Test assignment is splitted into two parts.
This task can be complitted with Django or Flask frameworks

## Task content: 
### Part 1 (required) 
1. Create a web page that displays employee hierarchy in a tree form.
  * Employee   data   should   be   stored   in   a   database,   following   information   about  
each employee is required: 
     ○ Full name; 
     ○ Position; 
     ○ Employment start date; 
     ○ Salary. 
  * Every employee has exactly 1 boss; 
  * Database   should   be   filled   in   with   data   of   at   least   50,000   employees   and   there  should be at least 5 levels of hierarchy; 
  * Don’t forget to display employee positio
2. Create database using Django / Flask migrations. 
3. Use Django ORM / Flask-SQLAlchemy seeder to fill database with data. 
4. Use Twitter Bootstrap to apply basic styles to your page. 
5. Using   standard   Django   /   Flask   functionality   implement   login/password   restricted  
area of the website. 
6. In   this   login/password   restricted   area   сreate   another   web   page   with   a   list   of   all  
employees   with   all   employee   record   fields   from   the   database   and   implement  
possibility to order by any field. 
7. Add possibility to search by any field to the page you created in task 6. 
8. Add   possibility   to   order   (and   search   if   task   7   is   implemented)   by   any   field   without  
reloading the whole page (i.e. using ajax). 
9. In   the   login/password   restricted   area   implement   the   rest   of   CRUD   functionality   for  
employee   record.   Please   note   that   all   employee   fields   should   be   editable   including  
possibility to change employee’s boss. 
10. Implement   possibility   to   upload   employee   photo   and   display   it   on   the   employee   edit  
page   and   add   additional   column   with   small   resized   employee   photo   to   the  
employee list page. 

### Part 2 (optional)
1. Implement   logic   to   re-assign   employee’s   subordinates   to   employee’s   boss   in   case   if  
employee   is   being   deleted   (additional   bonus   points   if   you   implement   it   using   Django  
ORM / Flask-SQLAlchemy ORM features). 
2. Implement   lazy   loading   for   employee   tree,   i.e.   by   default   show   first   2   levels   of  
hierarchy   and   load   tree   branch   (full   or   2   more   levels   of   hierarchy)   by   clicking   on   the  
employee from the 2nd level. 
3. Implement   possibility   to   change   employee’s   boss   using   drag-n-drop   directly   in   the  
employee tree. 
