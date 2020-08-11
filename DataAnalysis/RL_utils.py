import os
import matplotlib.pyplot as plt
import numpy as np
from JSAnimation import IPython_display
from matplotlib import animation
import matplotlib.patches as mpatches
import cv2
import imageio
import mpld3
import scipy.misc

def plot_movie_js2(enc_array,image_array,save=None):
    #Shows encoding and frames
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.title('Visual Encoding', fontsize=15)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.title('Vector Encoding', fontsize=15)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    ax3 = fig.add_subplot(1, 2, 2)
    im3 = plt.imshow(image_array[0])
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

    def animate(i):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_array(image_array[i])
        return (im,)
    
    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))

    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)
        
def save_movie_js2(enc_array,image_array,save=None):
    #dpi = 72.0
    #xpixels, ypixels = image_array[0].shape[0], image_array[0].shape[1]
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.title('Visual Encoding', fontsize=15)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.title('Vector Encoding', fontsize=15)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    ax3 = fig.add_subplot(1, 2, 2)
    im3 = plt.imshow(image_array[0])
    plt.axis('off')

    for i in range(enc_array.shape[0]):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_array(image_array[i])
        #plt.savefig(path+save+'/img'+str(i).zfill(4)+'.png', bbox_inches='tight')
        plt.savefig(save+'/img'+str(i)+'.png', bbox_inches='tight')
        
def plot_movie_jsInfo(enc_array,image_array,acts,vals,rews,save=None):
    
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
        plt.title('Visual Encoding', fontsize=15)
    else:
        icaLen = enc_array[0][0].shape[0]
        im = plt.imshow(enc_array[0][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Visual Encoding - ICs', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
        plt.title('Vector Encoding', fontsize=15)
    else:
        im2 = plt.imshow(enc_array[1][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Vector Encoding - ICs', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    

    
    def animate(i):
        if not isinstance(enc_array,list):
            im.set_array(enc_array[i][:8,:])
            im2.set_array(enc_array[i][8:,:])
        else:
            im.set_array(enc_array[0][i].reshape(1,icaLen))
            im2.set_array(enc_array[1][i].reshape(1,icaLen))
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        return (im,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)

def save_movie_jsInfo(enc_array,image_array,acts,vals,rews,save=None):
    
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
        plt.title('Visual Encoding', fontsize=15)
    else:
        icaLen = enc_array[0][0].shape[0]
        im = plt.imshow(enc_array[0][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Visual Encoding - ICs', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
        plt.title('Vector Encoding', fontsize=15)
    else:
        im2 = plt.imshow(enc_array[1][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Vector Encoding - ICs', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    
    if isinstance(enc_array,list):
        a_len = rews.shape[0]
    else:
        a_len = enc_array.shape[0]
    
    for i in range(a_len):
        if not isinstance(enc_array,list):
            im.set_array(enc_array[i][:8,:])
            im2.set_array(enc_array[i][8:,:])
        else:
            im.set_array(enc_array[0][i].reshape(1,icaLen))
            im2.set_array(enc_array[1][i].reshape(1,icaLen))
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        plt.savefig(save+'/img'+str(i).zfill(4)+'.png', bbox_inches='tight')

def plot_movie_js3(enc_array,image_array,cluster, save=None):
    #Plot Encodings and frames + information about which cluster the frame is in
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    plt.title('Visual Encoding', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    plt.title('Vector Encoding', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    plt.axis('off')
    im4 = plt.imshow(image_array[0])
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.3,0.1,'Cluster ' + str(cluster[0]), fontsize=20,color='white',bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

    def animate(i):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_text('Cluster ' + str(cluster[i]))
        im4.set_array(image_array[i])
        return (im,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)

def plot_actions(act):
    fig = plt.figure(figsize=(7,10))
    fig.suptitle('Distribution of Actions', fontsize=20)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.hist(act[:,0,0],bins=np.linspace(-0.4,2.6,4),color='chocolate',width=0.8)
    plt.title('Move Forward/Back', fontsize=15)
    plt.xticks(np.arange(3),['Stand','Forward','Back'], fontsize=13)
    ax2 = fig.add_subplot(2, 2, 2)
    plt.hist(act[:,0,1],bins=np.linspace(-0.4,2.6,4),color='chocolate',width=0.8)
    plt.title('Camera', fontsize=15)
    plt.xticks(np.arange(3),['Straight','Left','Right'], fontsize=13)
    ax3 = fig.add_subplot(2, 2, 3)
    plt.hist(act[:,0,2],bins=np.linspace(-0.4,1.6,3),color='chocolate',width=0.8)
    plt.title('Jump', fontsize=15)
    plt.xticks(np.arange(2),['Stand','Jump'], fontsize=13)
    ax4 = fig.add_subplot(2, 2, 4)
    plt.hist(act[:,0,3],bins=np.linspace(-0.4,2.6,4),color='chocolate',width=0.8)
    plt.title('Move Left/Right', fontsize=15)
    plt.xticks(np.arange(3),['Stand','Right','Left'], fontsize=13)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

def correlate(enc,val,num=0,normalize=False):
    corrs = []
    v = val#[:,0,num]
    if normalize:
        v = (v - np.mean(v)) /  np.std(v)
    for i in range(enc.shape[-1]):
        e = enc[:,i]
        if normalize:
            e = (e - np.mean(e)) / (np.std(e) * len(e))
        #corr = np.correlate(e,v)
        corr = np.corrcoef(e,v)[0,1]
        corrs.append(float(corr))
    return np.array(corrs)

def plot_movie_curInfo(enc_array,image_array,pred_s,enc_cur,acts,vals,rews,range_vis,range_vec,save=None):
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(3, 3, 1)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im = plt.imshow(enc_array[0][:4,:],vmin=range_vis[0], vmax=range_vis[1])
        plt.title('Visual Encoding', fontsize=15)
    else:
        icaLen = enc_array[0][0].shape[0]
        im = plt.imshow(enc_array[0][0].reshape(1,icaLen))
        plt.title('Visual Encoding - ICs', fontsize=15)
    ax2 = fig.add_subplot(3, 3, 2)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im2 = plt.imshow(enc_array[0][4:,:],vmin=range_vec[0], vmax=range_vec[1])
        plt.title('Vector Encoding', fontsize=15)
    else:
        im2 = plt.imshow(enc_array[1][0].reshape(1,icaLen))
        plt.title('Vector Encoding - ICs', fontsize=15)
       
        
    ax5 = fig.add_subplot(3,3,4)
    plt.axis('off')
    im5 = plt.imshow(pred_s[0][:4,:],vmin=range_vis[0], vmax=range_vis[1])
    plt.title('Predicted')
    
    ax6 = fig.add_subplot(3,3,5)
    plt.axis('off')
    im6 = plt.imshow(pred_s[0][4:,:],vmin=range_vec[0], vmax=range_vec[1])
    plt.title('Predicted')
    
    ax7 = fig.add_subplot(3,3,7)
    plt.axis('off')
    im7 = plt.imshow(enc_cur[0][:4,:],vmin=range_vis[0], vmax=range_vis[1])
    plt.title('Actual')
    
    ax8 = fig.add_subplot(3,3,8)
    plt.axis('off')
    im8 = plt.imshow(enc_cur[0][4:,:],vmin=range_vec[0], vmax=range_vec[1])
    plt.title('Actual')
    
    ax4 = fig.add_subplot(1, 3, 3)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 3, 3)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    
    def animate(i):
        if not isinstance(enc_array,list):
            im.set_array(enc_array[i][:4,:])
            im2.set_array(enc_array[i][4:,:])
        else:
            im.set_array(enc_array[0][i].reshape(1,icaLen))
            im2.set_array(enc_array[1][i].reshape(1,icaLen))
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        
        im5.set_array(pred_s[i][:4,:])
        im6.set_array(pred_s[i][4:,:])
        im7.set_array(enc_cur[i][:4,:])
        im8.set_array(enc_cur[i][4:,:])
        return (im,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)
        
def plot_movie_semantic(semantic,image_array,acts,vals,rews,save=None):
    
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(1, 2, 1)
    plt.axis('off')
    lbls = np.rot90(np.array([int(n) for n in semantic[0][1:-4].split(",")]).reshape((128,128)))
    im1 = plt.imshow(lbls,vmin=-1,vmax=10,cmap='tab20')
    values = np.linspace(-1,10,12)
    colors = [ im1.cmap(im1.norm(value)) for value in values]
    patches = [ mpatches.Patch(color=colors[i], label=inv_map[values[i]] ) for i in range(len(values)) ]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )
    
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    

    
    def animate(i):
        try:
            lbls = np.rot90(np.array([int(n) for n in semantic[i][1:-4].split(",")]).reshape((128,128)))
            im1.set_array(lbls)
        except:
            broken = np.array([int(n) for n in data[i][1:-4].split(",")])
            lbls = np.rot90(np.append(broken,np.zeros((128*128)-broken.shape[0])).reshape((128,128)))
            im1.set_array(lbls)
            print(str(i)+" - "+str(broken.shape))
        
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        return (im1,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)
        
def plot_movie_semantic2(semantic,image_array,acts,vals,rews,save=None):
    label_dict = {"Unknown": 0,
              "Agent": 1,
          "Level Door": 2,
          "Regular Door": 3 ,
          "Key Door": 4 ,
          "Entry Door": 5 ,
          "Puzzle Door": 6 ,
          "Key": 7 ,
          "Time Orb": 8 ,
          "Wall":9,
          "Floor": 10}
    inv_map = {v: k for k, v in label_dict.items()}
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(1, 2, 1)
    plt.axis('off')
    im1 = plt.imshow(rgb2L(semantic[0]),vmin=0,vmax=11,cmap='tab20')
    values = np.linspace(0,10,11)
    colors = [ im1.cmap(im1.norm(value)) for value in values]
    patches = [ mpatches.Patch(color=colors[i], label=inv_map[values[i]] ) for i in range(len(values)) ]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )
    
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"0 R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    

    
    def animate(i):
        try:
            im1.set_array(rgb2L(semantic[i]))
        except:
            print(str(i)+" - "+str(broken.shape))
        
        im3.set_text(str(i)+" R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        return (im1,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)

def rgb2L(img):
    l_img = np.zeros((img.shape[0]*img.shape[1]))
    for i,p in enumerate(img.reshape(img.shape[0]*img.shape[1],3)):
        if (p[0] in range(5,15) and p[1] in range(0,2) and p[2] in range(65,75)):
            l_img[i] = 1#Agent
        elif(p[0] in range(60,70) and p[1] in range(62,67) and p[2] in range(22,30)):
            l_img[i] = 2#Level Door
        elif(p[0] in range(30,50) and p[1] in range(65,105) and p[2] in range(30,50)):
            l_img[i] = 3#Green Door
        elif(p[0] in range(60,70) and p[1] in range(30,35) and p[2] in range(30,35)):
            l_img[i] = 4#Key Door
        elif(p[0] in range(27,32) and p[1] in range(30,35) and p[2] in range(25,45)):
            l_img[i] = 5#Entry Door
        elif(p[0] in range(55,80) and p[1] in range(35,50) and p[2] in range(75,110)):
            l_img[i] = 6#Puzzle Door
        elif(p[0] in range(50,70) and p[1] in range(60,80) and p[2] in range(0,20)):
            l_img[i] = 7#Key
        elif(p[0] in range(5,15) and p[1] in range(60,74) and p[2] in range(65,85)):
            l_img[i] = 8#Orb
        elif(p[0] in range(0,2) and p[1] in range(0,2) and p[2] in range(0,2)):
            l_img[i] = 9#Wall
        elif(p[0] in range(45,60) and p[1] in range(38,50) and p[2] in range(22,26)):
            l_img[i] = 10#Floor
        else:
            l_img[i] = 0#Other
    return l_img.reshape((img.shape[0],img.shape[1]))