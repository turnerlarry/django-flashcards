from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})

def add(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)
	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
			color = "primary"
		else:
			my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_answer) + " not " + answer
			color = "danger"

		return render(request, 'add.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color': color,
			})

	return render(request, 'add.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def subtract(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)
	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
			color = "primary"
		else:
			my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + " = " + str(correct_answer) + " not " + answer
			color = "danger"

		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color': color,
			})

	return render(request, 'subtract.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def multiply(request):
	from random import randint
	num_1 = randint(0,12)
	num_2 = randint(0,12)
	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
			color = "primary"
		else:
			my_answer = "Incorrect! " + old_num_1 + " x " + old_num_2 + " = " + str(correct_answer) + " not " + answer
			color = "danger"

		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color': color,
			})

	return render(request, 'multiply.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

