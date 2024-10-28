# SC1015 Project

# Problem Statement: Predicting Game Success on Steam Based on Release Features

The video game industry has become a vast and competitive market, with thousands of games released each year on platforms like Steam. However, only a subset of these games achieve high success, often measured by popularity, player engagement, and positive reception. Despite the abundance of data on released games, it remains challenging for developers and publishers to identify which specific release characteristics contribute most significantly to a game's success.

This project seeks to develop a predictive model to forecast game success using features available at release. Success metrics, including peak concurrent users (`peak_ccu`), positive reviews (`positive`), and estimated owners (`estimated_owners`), will serve as proxies for a game's success. The primary aim is to help developers, publishers, and industry stakeholders make informed decisions about game design, pricing, and marketing strategies to increase the likelihood of success on Steam.

### The analysis will explore the following release features as predictors:
- **Game price (`price`)**
- **Age restriction (`required_age`)**
- **Downloadable content count (`dlc_count`)**
- **Developer and publisher**
- **Game categories (e.g., multiplayer, single-player)**
- **Genres (e.g., action, strategy, RPG)**

Using regression analysis and feature importance ranking, the project will assess the individual and combined effects of these variables on success outcomes. The results could reveal which factors—such as pricing, genre choice, or platform availability—are most correlated with user engagement and satisfaction. 

Ultimately, the model aims to serve as a tool for better decision-making in game development and marketing, addressing the industry's need for evidence-based strategies to increase game success.

