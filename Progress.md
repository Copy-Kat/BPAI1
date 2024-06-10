# Recipe NERC

## Related works/citations
- [Comparison of Text Mining Models for Food and Dietary Constituent Named-Entity Recognition ](https://www.mdpi.com/2504-4990/4/1/12)
- [A Fine-Tuned Bidirectional Encoder Representations From Transformers Model for Food Named-Entity Recognition: Algorithm Development and Validation](https://www.jmir.org/2021/8/e28229/)
- [FINER dataset + Ensemble methods + comparison of methods](https://repository.pknu.ac.kr:8443/handle/2021.oak/32912)
- [RecipeDB + AllRecipes dataset](https://www.researchgate.net/publication/347066216_RecipeDB_a_resource_for_exploring_recipes)
- [FoodBase corpus](https://academic.oup.com/database/article/doi/10.1093/database/baz121/5611291) - not fit for use case
- [Data processing and techniques](https://arxiv.org/pdf/2004.12184.pdf)
- [Intro to CRF](https://arxiv.org/abs/1011.4088)
- [Bi-LSTM CRF](https://arxiv.org/abs/1508.01991)
- [Efficiently introduce features to CRF](https://arxiv.org/abs/1212.2504)


## Progress

### Phase 0: Data collection 

#### Data sources: FINER dataset + RecipeDB + AllRecipes + group24 recipe DB

#### Preprocessing:

- FINER:
    - Starts in conll format but only has the token + class (in IOB format)
    - Concat all the words with " ".join to form full sentences and pass it to spacy to get more features (POS, Shape, ...)
    - Export the file as csv (could use conll but no good libraries)
    - Has the largest amount of info (1.3 mil tokens - 180k sentences)
    - Collected and processed from AllRecipes
    - Has some extra features: 
        - Standardized the unit and quantity measurements: convert '/' numbers to proper floats (1/2 -> 0.5) and units to their full version (tbps -> tablespoon)

- RecipeDB + AllRecipes:
    - Starts in tsv format, same info as FINER but already splited in train + test set
    - We could do the same concat operation but the result does not work well with spacy (different tokenisation algorithm) so we just pass the raw tokens to the Stanford Tagger for POS tags
    - Export the file as csv (with less info)
    - Medium size: ~50k tokens in total

- Group24 recipe DB:
    - Starts as pl files
    - We could extract the ingredients and quantities for initial training data
    - Steps could be second stage
    - Ingredient could be used as annotation/gold labels
    - All could be added to a csv and tokenise with spacy
    - Known problems so far:
        - Spice is somewhat inconsistent on whether they are included (salt, pepper)
        - Ingredients some are shorten (potato for all potatos, ...), also inconsistent

### Phase 1: Regex

Best performing regex on PCA db (ingredients and quantities) + FINER: 

```text
([0-9]*\.?[0-9]*) ?(\( ([0-9]*) ([a-z]*) \))? ([a-z]*) (.*)
```

#### Explain:

- First group: capturing the quantities in form "&lt;number&gt;.&lt;number&gt;"
- Second group: capturing alternate unit (in form "( &lt;quantity&gt; &lt;unit&gt; )")
    - First group inside: capturing the quantity
    - Second group inside: capturing the unit
- The second group is optional as some text wont include any alt units
- Third group: capturing the base unit
- Fourth group: capturing the ingredient

#### Notes:
- Made for a very specific sentence structure:

```text
<number>.<number> ( <number> <unit> )? <unit> <preposition>? <ingredient>
```
- This is the most common structure so far, thus resulting the in best extraction of enities
- Does not work on other structures (just 'salt' for example)
- Current issues:
    - The format used here need to have the quantity be normalised to a float (1 1/4 won't work)
    - The unit should also be seperated (consequence from the processing of FINER)
    - It is not possible to persicely extract the ingredient name from other factors ("fresh apricots pitted and quartered" for example, there are too many different structures/words to be considered). We could add the use of lexicon/dictionary for it but it is hard to achive good accuracy.

#### Findings:
- The POS of the words seems to be very important. We can pickup on noun phrases with this and thus could limit the range in a more messy document.
- The range around the word of interest seems to be reletively short ((+-)1-2 words window).
- Using lexicon could quickly extract commonly used ingredients like spices as well as helping the model picking up on the units of measures for more context clues
- We should have a couple steps of preprosessing to convert the sentence to what the model would expects

### Phase 2: CRF

#### Methodology:
- Start with a basic model (general settings)
- Add more features efficiently using algorithm
- Build a Bi-LSTM model (best performance)
- Evaluate

#### Basic model:
- Standard setings using sklearn_crfsuite with basic features (general model used for typical NER tagging task)
- No fine-tuning yet
- Reletively good performance on FINER but a bit weaker on recipeDB
- Good performance on FINER due to simple structure?



## TODOs:
- [x] Clean + concat data - done for 1 set, might be sufficient?
- [x] Build some core regexes
- [x] Build regex testing script
- [x] Collect main findings on regex
- [x] Build basic CRF model
- [ ] Add algorithm for adding features
- [ ] Add LSTM layer
- [ ] Evaluate all models
- [ ] Decide on transformer approach

## Notes:
- POS tagger to use? Stanford vs SpaCy
    - SpaCy might be better. Stanford is rulebased while Spacy is statistical. Preliminary test implied that both have comparable performance but Spacy give more features for latter usage
    - Stanford can be used when only tokens are provided and there's no easy way to pass it to SpaCy
- Data processing pipeline:
    - Add space in between quantity and units (if needed)
    - Convert all quantity to 1 float (1 1/2 -> 1.5)
    - Remove everything in bracket
    - Remove quotes 



- Describe the PCA dataset
    - Add ID, INQ, Ingredients

apply regex
-> analyse using metrics
-> identify key issues
-> fix the data after the application
-> use that to train crf

add more datial desc of metrics (matching percentage)
-> aggreagte per recipes -> means/standard deviations

-> write down as a formula (accuracy)

note down the problems to be decided 

more percise in wording (INQs, ...)

add 





ingredient phrases from recipe texts

using insights from regex to improve the accuracy 

small paraghaph motivate why we want this question, after question high level on how to achive the question

- basic nlp -> see the limits -> see if we can use crf

address the research the question, not answering the question.

add that ingredient as the ground truth

make PCA simple, move the prolog stuff to the footnotes

refrence the confluence page

add more text for 3.3 for more clarity 

put 3.5 to its own section (4) make regex as 

chapter 3 -> data

chapter 4 -> approach (regex)

chapter 5 
