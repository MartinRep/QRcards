from flask import Flask, render_template, request, make_response, redirect
import os
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('pdfUpload.html')


@app.route("/uploadbill", methods=['POST'])
def processImage():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("saved file successfully")
      #send file name as parameter to downlad
            return redirect('/downloadfile/'+ filename)
    return render_template('upload_file.html')
    # dev only - save processed image
    # img.save('uploads/submitted.png', format="png")
    # return "TEST"


if __name__ == '__main__':
    app.run(host='0.0.0.0')