######### superimpose tweet locations on map of places   ##########

latt = read.csv("/Users/Neo/Documents/LearnPython/poke_latt.csv")
long = read.csv("/Users/Neo/Documents/LearnPython/poke_long.csv")

coord = cbind(long,latt)
colnames(coord) = c("Longitude","Latitude")

library(maps)
library(ggmap)

chicago = get_map(location = "chicago", zoom = 10)
california = get_map(location = "california", zoom = 7)
usa = get_map(location = "USA", zoom = 4)

# tweet locations superimposed on maps of places
ggmap(chicago) + geom_point(data = coord, aes(x = Longitude, y = Latitude))
ggmap(california) + geom_point(data = coord, aes(x = Longitude, y = Latitude))
ggmap(usa) + geom_point(data = coord, aes(x = Longitude, y = Latitude), color="red")

# Round latitude and longitude to 1 digit of accuracy, and create a crime counts data frame for each area:
LatLonCounts = as.data.frame(table(round(coord$Longitude,1), round(coord$Latitude,1)))

#str(LatLonCounts)

LatLonCounts$Long = as.numeric(as.character(LatLonCounts$Var1))
LatLonCounts$Lat = as.numeric(as.character(LatLonCounts$Var2))

# Plot these points on our map:
# Change the color scheme:
ggmap(usa) + geom_point(data = LatLonCounts, aes(x = Long, y = Lat, color = Freq, size=Freq)) + scale_colour_gradient(low="yellow", high="red")

ggmap(usa) + geom_tile(data = LatLonCounts, aes(x = Long, y = Lat, alpha = Freq), fill="red")

ggmap(california) + geom_tile(data = LatLonCounts, aes(x = Long, y = Lat, alpha = Freq), fill="red")
