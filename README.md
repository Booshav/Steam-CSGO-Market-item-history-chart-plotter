# Steam-CSGO-Market-item-history-chart-plotter
This python code gives you a visualization of a specific item of your choice from the steam market.

Thank you for using my steam item market history visualizer!

The app has no UI, therefore it is console/shell based.

Setup:

In the python file (SteamPriceChart.py), you have to replace "steamLoginSecure" with your steamLoginSecure network header.
  > To do this:
  -Open steam on your browser
  -Inspect the site(open the inspector)
  -In the inspector, navigate to the "Network" tab
  -On the site, navigate to the "Market"
  -Under the network tab, find the request with domain "steamcommunity.com", and find the "Cookies" tab on the right side
  -From the "Cookies" tab, you should see a dictionary with your steamLoginSecure written on it.
  -Copy the steamLoginSecure, and paste it in your code on line 66(Next to the aforementioned variable name)
  
 Usage:
  > To access an item in the CSGO Steam market, you need it's full name(IT IS CASE SENSITIVE!)
  -Type the name once prompted to, after starting the application
  -Select your timeframe(1 week, 1 month, or it's whole price history)
 
Check for spelling mistakes in case the app doesnt recognize your input!
