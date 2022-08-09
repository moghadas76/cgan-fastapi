import torch
import matplotlib.pyplot as plt
from torchvision import transforms
from datetime import datetime
from model import Generator

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model_path = 'generator_200.pth'
model = Generator()
# model = torch.nn.DataParallel(model)
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

def generator_inference(label, device=device):
  noise_vector = torch.randn(24, 100, device=device)  
  noise_vector = noise_vector.to(device)
  labels = torch.tensor([label]* 24, device=device).reshape(24, 1)
  r_generated_image = model((noise_vector, labels))
  return_values = []
  for i in range(24):
    plt.imshow(transforms.ToPILImage()(r_generated_image[i,...]))
    value = f"{str(datetime.now().timestamp())}.png"
    return_values.append(value)
    plt.savefig(value)
  return return_values
