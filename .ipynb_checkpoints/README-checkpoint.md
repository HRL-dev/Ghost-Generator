# Ghost Story Generator

### Let's build ghost stories!

## Problem Statement

I'm building a ghost story generator! I want to be able to generate something resembling a Victorian-era ghost story using NLP. Ghost stories are rad, and NLP is even more rad. Let's do this.


## How It Went

So, first things first, I had to get some ghost stories to use to train a model. Obviously I need to have permission to use those stories, and the best place to find books with open permissions is [Project Gutenberg](http://www.gutenberg.org/). I chose a book of classic ghost stories called [The Best Ghost Stories](http://www.gutenberg.org/files/17893/17893-h/17893-h.htm), ed. by Arthur E. Reeve, published in 1919, which puts all of the stories within it at exactly the right era for the flavor of ghost story that I'm looking for. I used an awesome package called [Gutenberg](https://pypi.org/project/Gutenberg/) that scraped the story and processed the html soup for me, and then I sliced the text up into individual stories and cleaned up any unwanted characters.

Now, it's time to model! When it comes to NLP, at the moment, no models are better than OpenAI's [Generative Pre-trained Transformers](https://openai.com/blog/openai-api/). They recently released GPT-3, which is apparently completely astonishing in its ability to generate text resembling human output, but it is currently under exclusive license and not available for use by various unknown data scientists such as myself. So, I chose to use [GPT-2](https://openai.com/blog/gpt-2-1-5b-release/), which is also truly amazing as far as text generation results go.

I fine-tuned GPT-2 using [this Google Colab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) and [this GPT-2 package](https://pypi.org/project/gpt-2-simple/) called gpt-2-simple. I was not going to be able to fine-tune the model on my own machine because even the smallest version of it (124M) is absolutely enormous, so I used Google Colab's cloud-based GPU. I entered in the text of the ghost stories I selected, then ran the model and downloaded the result - and now I can generate ghost stories on my own computer! Magical.

## Results

Let's look at a few snippets of the ghost stories GPT-2 wants to tell us:

"Both are from the Northern Territory. They were both murdered in their sleep. There was no watchmen on duty at the time, and the boys had no nightscreens.  The corpses of the two policemen were moved to a small dark room in the back of the house, to be moved a cold dark from the night before.  The bushes outside the window seemed to be turned down, and the drywall, to which the ghostly clouds dragged in, with their hint of the decay of the fir tree, was hauled up into the sky.  Ghosts are not unheard of in our tales."

Truly frightening. Then there was this one, in which the model seemed to become extremely interested in sparkling wine in particular:

"The journey home was now over, and I felt sure that my servant was returning with two bottles of bitter wine and a jug of sparkling water. He had brought with him several curious bottles of wine--the standing-room-only bottles--that had been lost under the deluge two weeks ago in the torrent of molasses that had dumped them. The first specimen I saw of the kind produced in Germany was a bottle of sparkling wine (that has not been mentioned in this connection anguishing from the bottles), a bottle of silver, and a glass of fine sparkling wine. As the feeling for the valuable wine returned I felt a change in my companion's attitude; his eagerness was much illumined by the unaccountable sweetness the water in the bottles. Even then it was surprising to see such a beautiful animal among the spoils of valor among people of exceptional learning and talent."

I don't know about you, but I request NOT to drink wine that was dumped by a torrent of molasses, sparkling or not.

As you can see, although some of the sentences make only a middling amount of sense, the text generation abilities of GPT-2 are truly amazing. Even if there are some mistakes, the output of the model still resembles a Victorian-era ghost story in both content and language. I call that a success!

## Can I Generate My Own Ghost Stories?

Short answer: [you can try!](https://ghost-generator.herokuapp.com/)

Longer answer: after getting my model to generate stories, I moved on to building a flask app so other people could generate ghost stories, too. I designed the flask app to be simple but effective: you push a button and you get a ghost story!

In deploying the app to Heroku, I ran into several million bugs. The final bug was a giant cockroach that I wasn't sure I could overcome: the version of tensorflow necessary to the gpt-2-simple package that contained my model was breaking in my Heroku instance.

## What's Next?

There are several things I'd like to do with this project in the future: I want to train a few more books of Victorian ghost stories scraped from Project Gutenberg to make the resulting stories even more fleshed out. I'd love to get a chance to use a GPT-3 model on this project, because I think it could put out stories that actually have a narrative flow that makes more sense. Finally, I'd love to get a functioning, visitable site that people can go to where the MODEL ACTUALLY RUNS.

## Bibliography

- [Project Gutenberg](http://www.gutenberg.org/)
- [The Best Ghost Stories](http://www.gutenberg.org/files/17893/17893-h/17893-h.htm)
- [Gutenberg](https://pypi.org/project/Gutenberg/)
- [Generative Pre-trained Transformers](https://openai.com/blog/openai-api/)
- [GPT-2](https://openai.com/blog/gpt-2-1-5b-release/)
- [Google Colab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce)
- [GPT-2 package](https://pypi.org/project/gpt-2-simple/)
- [Max Woolf](https://minimaxir.com/2019/09/howto-gpt2/): this is the blog of the creator of the gpt-2-simple package & google colab notebook that I used to create my model.

