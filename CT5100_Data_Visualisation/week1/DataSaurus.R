library(datasauRus)
library(dplyr)
library(kableExtra)
datasaurus_dozen %>%
  group_by(dataset) %>%
  summarize(
    mean_x    = mean(x),
    mean_y    = mean(y),
    std_dev_x = sd(x),
    std_dev_y = sd(y),
    corr_x_y  = cor(x, y)
  )%>%kbl()%>%
  kable_classic(full_width = F, html_font = "Cambria")


library(ggplot2)
ggplot(datasaurus_dozen, aes(x = x, y = y))+
  geom_point(size =0.8, colour="black", alpha = 0.8)+
  theme_void()+
  facet_wrap(~dataset, ncol = 3)