import streamlit as st

# Introduction Section
st.header("Conclusion")
st.write("This chapter shows the conclusions of the project")

# Bullet points with the conclusions
st.write("The following are the conclusions of the project, according to the research objective and questions posed:")
st.markdown("- Throughout this document, an algorithm for placing inspectors in the Dutch Motorway Network was devised, "
            "implemented, and tested, as intended when setting the main objective of the assignment. As explained in previous "
            "chapters, the optimal location depends on the desired number of inspectors to place, and as such there exists a "
            "trade-off between this value, the response time and network coverage. Our algorithm correctly identifies the areas "
            "in which an accident is more likely to occur and assigns inspectors accordingly.")
st.markdown("- For reaching the research objective, the algorithm takes as starting point the incident dataset provided by "
            "Rijkswaterstaat, and the Rijkswegen road network Shapefile. In consequence, the results provided are representative "
            "of the temporal and geographic context in which information was gathered. Even though validation and simulation procedures "
            "were implemented to assess the placement strength, it is important to use different datasets to increase the "
            "representativeness of the results.")
st.markdown("- When analysing the spatial distribution of incidents in the Netherlands, 8 cluster zones could be identified; among them, "
            "the Randstad area (Amsterdam – The Hague – Rotterdam) contains the vast majority of incident points followed by the "
            "Eindhoven metropolitan region, and the northeast and southwest regions contained the fewest points. Now, when it comes to "
            "the temporal distribution of incidents, it is important to highlight that accidents and vehicle obstructions were more "
            "frequent in the evening peak and in the morning peak, while general obstructions tend to happen in the afternoon before"
            "the evening peak; on the other hand, Thursdays and Fridays  were the days when more incidents occurred, while Wednesdays "
            "had the lowest accident count; finally, November was the month with the lowest incident count, but when it comes to "
            "accidents only, August had the lowest count.")
st.markdown("- Two main statistical analyses were conducted to determine the probability of an accident happening at a certain location. "
            "In the first place, a lognormal distribution was fit to the daily accident count to determine the probability that a "
            "certain accident number occurs in a single day. Then, and a nonparametric distribution was fit to the accidents location "
            "using Kernel Density Estimation (KDE), so that the accident probability of a network segment could be calculated, and "
            "ultimately samples of accidents locations in a typical day could be drawn.")
st.markdown("- The way the algorithm works, inspector placement is conditioned by the spatial incident density and the desired number of "
            "inspectors. However, the spatial incident density function can be calculated for the dataset as a whole or for a specific "
            "subset, meaning that the user can filter the dataset according to specific criteria and get an inspector placement "
            "accordingly. The inspector response time can be broken down into the time it takes between an incident happens and it is "
            "reported, the time it takes to determine which inspector should attend the incident, and the travel time of that inspector "
            "to the incident; the scope of this project only concerns the latter calculation.")
st.markdown("- Inspector travel time to the incident is calculated by determining the shortest path between their location and the "
            "incident’s location using Dijkstra's algorithm. For this it is assumed that a inspectors can circulate at a speed of "
            "100 km/h without any limitations regarding traffic flow or lack of emergency lanes.")
st.markdown("- A script to calculate and plot the relationship between the number of inspectors and average travel time to incidents was "
            "generated. From the results it was evident that it is not possible to minimize both variables, as a trade-off exists "
            "between them. Therefore, the optimal number of inspectors would depend on other decision criteria, such as economic or "
            "supply chain constraints, quantitative aspects or other key performance indicators that are not addressed at the moment. "
            "However, it is important to note that the algorithm devised has enough flexibility to incorporate these elements.")

