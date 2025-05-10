from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.permanent_session_lifetime = timedelta(minutes=5)

movies = [
    {
        "id": 1,
        "title": "ექვსი და შვიდი",
        "director": "გენო ცაავას",
        "description": "ფილმის სათაურის გრაფიკული მხარე, უკიდურესად ურთიერთსაპირისპირო, დადებითისა და უარყოფითი ძალების მარადიულ მონაცვლეობას, მათი დაპირისპირებისა და ერთიანობის კონცეფციას ემსახურება. სადაც კაცობრიობის მიერ დაგლეჯილი დრო იდუმალ სიცხადედ იქცევა; ფილმი წარმოადგენს ცდას – ადამიანის ცნობიერების, კრისტალური გულისა და სულის გაღვიძებისა, ფასეულობათა გადაფასებისა, იმ სიძნელეთა დაძლევისა, რომელიც არსებობს როგორც ცოდვის შედეგად დაცემულ ქვეყნიერებაში – მატერიალურ სამყაროში, ასევე სულიერ არსებათა დასებში, რომელიც წარმართავს ისტორიულ პროცესს.",
        "year": 2003
    },
    {
        "id": 2,
        "title": "აბესალომ და ეთერი",
        "director": "ლეო ესაკიას",
        "description": "ეს არის ობოლი სოფლელი გოგონასა და კეთილი უფლისწულის ბედკრული სიყვარულის ისტორია. ცოლ-ქმარს შორის ბოროტ დემონად ჩადგება ვეზირი მურმანი, რომელსაც ისეთი თავდავიწყებით შეჰყვარებია თავისი პატრონის ულამაზესი მეუღლე, რომ მის ხელში ჩასაგდებად გრძნეულებს მიმართავს. სატრფოსთან დაშორება სტანჯავს აბესალომს, მისი სიკვდილით სასოწარკვეთილი ეთერიც გამოესალმება სიცოცხლეს.",
        "year": 1967
    },
    {
        "id":3,
        "title": "ბაგრატიონი",
        "director": " გიული ჭოხონელიძისა და გუგული მგელაძის",
        "description": "წარმოშობით ქართველმა მხედართმთავარმა მთელი ცხოვრება რუსეთის ინტერესებს შესწირა, რომელსაც თავის მეორე სამშობლოდ თვლიდა. მეომრული ვაჟკაცობის, ღირსების, სამშობლოსადმი ერთგულების სიმბოლოდ იქცა სახე გენერლისა, რომელმაც სამხედრო სამსახური სერჟანტობით დაიწყო",
        "year": 1985

    }


]

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session.permanent = True
        session['user'] = user
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return "ფილმი ვერ მოიძებნა", 404
    return render_template('movie_detail.html', movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
