# Food-Image-Recognition

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers](https://img.shields.io/github/stars/MaharshSuryawala/Food-Image-Recognition?style=flat-square)]()
[![Followers](https://img.shields.io/github/followers/MaharshSuryawala?style=flat-square)](https://github.com/MaharshSuryawala)
[![MIT License][license-shield]][license-url]
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/MaharshSuryawala/Food-Image-Recognition)

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Food-Image-Recognition](#food-image-recognition)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
    - [Overview](#overview)
    - [Built With](#built-with)
    - [Dataset](#dataset)
  - [Results](#results)
    - [Demo](#demo)
    - [Accuracy](#accuracy)
    - [Loss](#loss)
    - [Testing on random images.](#testing-on-random-images)
    - [Visualization of different layers.](#visualization-of-different-layers)
    - [Heat-Map & Class-Activation-Map](#heat-map--class-activation-map)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [References](#references)
  - [Acknowledgements](#acknowledgements)

## About the Project

![Food](.images/food.jpg)

<span>Photo by <a href="https://unsplash.com/@jaywennington?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Jay Wennington</a> on <a href="https://unsplash.com/s/photos/food?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

### Overview

* Each year, approximately 6,78,000 deaths are caused in the United States of America due to unhealthy diet. 
* A typical American diet is too high in calories, fat, sugars, sodium, etc. 
* Hence, people have became more proactive when it comes to health matters. 
* Services like eating habit recorder and calorie/nutrition calculator have became extremely popular. 
* They can make users aware of problems like obesity, cancer, diabetes, heart-disease, etc. that can be caused by unhealthy diets.
* Most of these services require the users to manually select a food item from a hierarchical menu which is a time consuming process and not so user friendly.   
* An user-interactive system that takes food images as an input, recognizes the food automatically and gives the nutritional-facts as an output will save a lot of time. 
* This system can be used in various areas such as social network, health-care applications, eating-habit evaluations, etc.
* For food image recognition we will be using transfer learning to retrain the final layer (with 101 additional food-classes) of Inception-v3 model which is already trained by Google on 1000 classes.
* It almost took 10-11 hours to train the model on Google Colab.    

### Built With

* [Python](https://www.python.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [Google Colab](https://colab.research.google.com/)

### Dataset


Food Images Source: [The Food-101 Data Set](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
  
  * The data set consists of 101 food categories, with 1,01, 000 images.
  * 250 test images/per class and 750 training images/per class are provided.
  * All the images were rescaled to have a maximum side length of 512 pixels. 

Nutrition Information Source: [Food Data Central API](https://fdc.nal.usda.gov/api-guide.html#bkmk-3)

  * U.S. Department of Agriculture, Agricultural Research Service. FoodData Central, 2019. fdc.nal.usda.gov. 

## Results

### Demo

![demo](.images/demo/food_image_recognition.gif)

### Accuracy

![Accuracy](.images/accuracy.png)

### Loss

![Loss](.images/loss.png)

### Testing on random images.

![Test](.images/test.png)

### Visualization of different layers.

![Layers](.images/layers.png)

### Heat-Map & Class-Activation-Map 

![Heatmap](.images/heatmap.png)

<!-- CONTRIBUTING -->
## Contributing  

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'feat: some amazing feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
[![Linkedin](https://api.iconify.design/openmoji:linkedin.svg?width=40&height=40)](https://www.linkedin.com/in/maharsh-suryawala-05410312b/) 

Maharsh Suryawala - [Portfolio](https://maharshsuryawala.github.io/maharshsuryawala/)

Project Link: [https://github.com/MaharshSuryawala/Food-Image-Recognition](https://github.com/MaharshSuryawala/Food-Image-Recognition)

## References

* [https://cspinet.org/eating-healthy/why-good-nutrition-important](https://cspinet.org/eating-healthy/why-good-nutrition-important)
* [https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Img Shields](https://shields.io)
* [Iconify](https://iconify.design/)
* [MIT License](https://opensource.org/licenses/MIT)
* [Unsplash](https://unsplash.com/)
* [Badgen](https://badgen.net/)
* [For The Badge](https://forthebadge.com/)


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MaharshSuryawala)


<!-- MARKDOWN LINKS -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MaharshSuryawala/Food-Image-Recognition?style=flat-square 
[contributors-url]: https://github.com/MaharshSuryawala/Food-Image-Recognition/graphs/contributors
[license-shield]: https://img.shields.io/github/license/MaharshSuryawala/Food-Image-Recognition?style=flat-square?style=flat-square
[license-url]: https://github.com/MaharshSuryawala/Food-Image-Recognition?style=flat-square/blob/master/LICENSE.txt
