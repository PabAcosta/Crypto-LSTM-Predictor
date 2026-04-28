# Crypto LSTM Closing Cost Predictor
The scope of this project is to create three LSTM models that predict three different coins. Each model will use $BTC and $ETH closing prices to predict their coins respective closing price. The three coins that will be tested are $DOGE, $SOL, and $XRP.

## Background
LSTM (Long Short Term Memory) Models are a type of Recurrent Neural Network that are used to handle sequences. Their main upside is that they are designed for long term dependency learning unlike more basic models that forget long term information. They work using a memory cell that carries information through the sequence. At each step, the model uses three components called gates. The forget gate removes unnecessary old information. The input gate adds new useful information. The output gate determines what to output. This process allows the model to update its memory and produce an output at each step.

## How to Run