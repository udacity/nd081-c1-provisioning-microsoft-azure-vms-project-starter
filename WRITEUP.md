# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

With the given use case, my decision is to go with App Service. This is detailed as following:

1. For cost availability and workflow, app service offers a reasonably low resource deployment. The user has to bear a consitent cost which has a significantly lower compute cost. Deployment process itself is less complex and python support is reasonably accomodative. 

2. VM offers more customization, howver has a higher complexty and cost and not needed in this usecase.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

More complex configuration needs or data types or significant build needs on the use case such as storing unstructred data with compute functions, would make a good use case to consider the verstality of VM however it would also mean budget the resource needs and therefore the cost factors.