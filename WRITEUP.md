# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
  
    |          | Cost     |  Scalability  | Availability  | Workflow  |
    |----------|----------|---------------|---------------|-----------|
    | App Service         | Free service available for small applications. And the cheapest offering is about $0.018           | Offers scaling options  | No SLA for the free service, but 99.95% SLA is available for non-freee services.         | Develop and deploy no access to underlying vms. Easy to use deployment options from a miriad  of sources. Limited programming languages use. | 
    | Virtual Machines    | No free service, but spot offering start price $0.0021/hour, and the pay-as-you-go cost starts at $0.0052/hour.  | Offers scaling options  | Minimum SLAs starting at 99% to 99.99% is available.          |  Develop and deploy with full control over application management and deployment. Deployment options from external source can become complex. No limit to programming languages that can be used to develop your application.      |
- *Choose the appropriate solution (VM or App Service) for deploying the app*
  
    > My choice was **App Service** based on the size of my deployment:
    
- *Justify your choice*
    - Cost: App Service offers a free service that meets my deployment needs.
    - Infrastructure Management: App Service manages my infrastructure and takes away a over head cost that goes with this.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.*

If the app configuration became more complex or needed heavy customizations, then I would use the virtual machine option. 
Virtual machines allow for more infrastructure customizations and is more cost effective, when compared to similar offerings on App Service.